import asyncio
import time
import urllib.robotparser
from collections import deque
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Iterable
from urllib.parse import urldefrag, urljoin, urlparse

import aiohttp
from bs4 import BeautifulSoup


@dataclass(slots=True)
class CrawledPage:
    job_id: str
    url: str
    title: str
    status_code: int | None
    depth: int
    links: list[str]
    response_time_ms: float
    success: bool
    crawled_at: str
    error: str | None = None


class ConcurrentCrawler:
    def __init__(
        self,
        job_id: str,
        seed_url: str,
        max_depth: int,
        max_concurrency: int,
        timeout_seconds: int = 15,
    ) -> None:
        self.job_id = job_id
        self.seed_url = self._normalize_url(seed_url)
        self.max_depth = max_depth
        self.max_concurrency = max_concurrency
        self.timeout = aiohttp.ClientTimeout(total=timeout_seconds)
        self.seed_host = urlparse(self.seed_url).netloc.lower()
        self.user_agent = "ConcurrentWebCrawler/1.0"

        if not self.seed_host:
            raise ValueError("seed_url must be an absolute URL")

    async def crawl(self) -> list[CrawledPage]:
        queue: deque[tuple[str, int]] = deque([(self.seed_url, 0)])
        seen = {self.seed_url}
        results: list[CrawledPage] = []
        semaphore = asyncio.Semaphore(self.max_concurrency)

        headers = {"User-Agent": self.user_agent}
        async with aiohttp.ClientSession(timeout=self.timeout, headers=headers) as session:
            robots = await self._load_robots_parser(session)

            while queue:
                current_depth = queue[0][1]
                batch: list[tuple[str, int]] = []

                # Processing one depth layer at a time keeps traversal BFS-style.
                while queue and queue[0][1] == current_depth:
                    batch.append(queue.popleft())

                pages = await asyncio.gather(
                    *(
                        self._fetch_page(session, semaphore, robots, url, depth)
                        for url, depth in batch
                    )
                )
                results.extend(pages)

                for page in pages:
                    if not page.success or page.depth >= self.max_depth:
                        continue

                    for link in page.links:
                        if link not in seen:
                            seen.add(link)
                            queue.append((link, page.depth + 1))

        return results

    async def _fetch_page(
        self,
        session: aiohttp.ClientSession,
        semaphore: asyncio.Semaphore,
        robots: urllib.robotparser.RobotFileParser,
        url: str,
        depth: int,
    ) -> CrawledPage:
        async with semaphore:
            if not robots.can_fetch(self.user_agent, url):
                return self._failed_page(url, depth, "Blocked by robots.txt")

            started_at = time.perf_counter()
            try:
                async with session.get(url, allow_redirects=True) as response:
                    content_type = response.headers.get("content-type", "")
                    body = await response.text(errors="ignore") if "text/html" in content_type else ""
                    elapsed_ms = (time.perf_counter() - started_at) * 1000
                    title, links = self._parse_html(body, str(response.url))

                    return CrawledPage(
                        job_id=self.job_id,
                        url=url,
                        title=title,
                        status_code=response.status,
                        depth=depth,
                        links=links,
                        response_time_ms=round(elapsed_ms, 2),
                        success=response.status < 400,
                        crawled_at=self._utc_now(),
                    )
            except asyncio.TimeoutError:
                elapsed_ms = (time.perf_counter() - started_at) * 1000
                return self._failed_page(url, depth, "Request timed out", elapsed_ms)
            except aiohttp.ClientError as exc:
                elapsed_ms = (time.perf_counter() - started_at) * 1000
                return self._failed_page(url, depth, str(exc), elapsed_ms)

    async def _load_robots_parser(
        self, session: aiohttp.ClientSession
    ) -> urllib.robotparser.RobotFileParser:
        robots_url = f"{urlparse(self.seed_url).scheme}://{self.seed_host}/robots.txt"
        parser = urllib.robotparser.RobotFileParser(robots_url)

        try:
            async with session.get(robots_url, allow_redirects=True) as response:
                if response.status < 400:
                    parser.parse((await response.text(errors="ignore")).splitlines())
                else:
                    parser.parse([])
        except (aiohttp.ClientError, asyncio.TimeoutError):
            # If robots.txt cannot be fetched, proceed as allowed rather than failing the crawl.
            parser.parse([])

        return parser

    def _failed_page(
        self,
        url: str,
        depth: int,
        error: str,
        response_time_ms: float = 0.0,
    ) -> CrawledPage:
        return CrawledPage(
            job_id=self.job_id,
            url=url,
            title="",
            status_code=None,
            depth=depth,
            links=[],
            response_time_ms=round(response_time_ms, 2),
            success=False,
            crawled_at=self._utc_now(),
            error=error or "Request failed",
        )

    def _parse_html(self, html: str, base_url: str) -> tuple[str, list[str]]:
        if not html:
            return "", []

        soup = BeautifulSoup(html, "html.parser")
        title_tag = soup.find("title")
        title = title_tag.get_text(strip=True) if title_tag else ""
        links = self._extract_internal_links(soup.find_all("a", href=True), base_url)
        return title, sorted(links)

    def _extract_internal_links(self, anchors: Iterable, base_url: str) -> set[str]:
        links: set[str] = set()

        for anchor in anchors:
            try:
                normalized = self._normalize_url(urljoin(base_url, anchor["href"]))
            except ValueError:
                continue

            parsed = urlparse(normalized)

            if parsed.scheme in {"http", "https"} and parsed.netloc.lower() == self.seed_host:
                links.add(normalized)

        return links

    @staticmethod
    def _normalize_url(url: str) -> str:
        parsed = urlparse(urldefrag(url.strip())[0])
        if parsed.scheme not in {"http", "https"}:
            raise ValueError("URLs must use http or https")

        normalized = parsed._replace(scheme=parsed.scheme.lower(), netloc=parsed.netloc.lower())
        return normalized.geturl().rstrip("/")

    @staticmethod
    def _utc_now() -> str:
        return datetime.now(timezone.utc).isoformat()
