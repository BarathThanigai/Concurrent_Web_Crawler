import asyncio
import time
from collections import deque
from dataclasses import dataclass
from typing import Iterable
from urllib.parse import urldefrag, urljoin, urlparse

import aiohttp
from bs4 import BeautifulSoup


@dataclass(slots=True)
class CrawledPage:
    url: str
    title: str
    status_code: int | None
    depth: int
    links: list[str]
    response_time: float
    success: bool
    error: str | None = None


class ConcurrentCrawler:
    def __init__(
        self,
        seed_url: str,
        max_depth: int,
        max_concurrency: int,
        timeout_seconds: int = 15,
    ) -> None:
        self.seed_url = self._normalize_url(seed_url)
        self.max_depth = max_depth
        self.max_concurrency = max_concurrency
        self.timeout = aiohttp.ClientTimeout(total=timeout_seconds)
        self.seed_host = urlparse(self.seed_url).netloc.lower()

        if not self.seed_host:
            raise ValueError("seed_url must be an absolute URL")

    async def crawl(self) -> list[CrawledPage]:
        queue: deque[tuple[str, int]] = deque([(self.seed_url, 0)])
        seen = {self.seed_url}
        results: list[CrawledPage] = []
        semaphore = asyncio.Semaphore(self.max_concurrency)

        headers = {"User-Agent": "ConcurrentWebCrawler/1.0"}
        async with aiohttp.ClientSession(timeout=self.timeout, headers=headers) as session:
            while queue:
                current_depth = queue[0][1]
                batch: list[tuple[str, int]] = []

                # Processing one depth layer at a time keeps traversal BFS-style.
                while queue and queue[0][1] == current_depth:
                    batch.append(queue.popleft())

                pages = await asyncio.gather(
                    *(self._fetch_page(session, semaphore, url, depth) for url, depth in batch)
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
        url: str,
        depth: int,
    ) -> CrawledPage:
        async with semaphore:
            started_at = time.perf_counter()
            try:
                async with session.get(url, allow_redirects=True) as response:
                    content_type = response.headers.get("content-type", "")
                    body = await response.text(errors="ignore") if "text/html" in content_type else ""
                    elapsed = time.perf_counter() - started_at
                    title, links = self._parse_html(body, str(response.url))

                    return CrawledPage(
                        url=url,
                        title=title,
                        status_code=response.status,
                        depth=depth,
                        links=links,
                        response_time=elapsed,
                        success=response.status < 400,
                    )
            except (aiohttp.ClientError, asyncio.TimeoutError) as exc:
                return CrawledPage(
                    url=url,
                    title="",
                    status_code=None,
                    depth=depth,
                    links=[],
                    response_time=time.perf_counter() - started_at,
                    success=False,
                    error=str(exc),
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
            normalized = self._normalize_url(urljoin(base_url, anchor["href"]))
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
