import json
import sqlite3
from pathlib import Path

from crawler import CrawledPage
from models import PageRecord, StatsResponse

DATABASE_PATH = Path(__file__).with_name("crawler.db")


class Database:
    def __init__(self, path: Path = DATABASE_PATH) -> None:
        self.path = path

    def initialize(self) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS pages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    url TEXT NOT NULL UNIQUE,
                    title TEXT NOT NULL,
                    status_code INTEGER,
                    depth INTEGER NOT NULL,
                    links TEXT NOT NULL,
                    response_time REAL NOT NULL,
                    success INTEGER NOT NULL,
                    error TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )

    def save_pages(self, pages: list[CrawledPage]) -> None:
        if not pages:
            return

        with self._connect() as connection:
            connection.executemany(
                """
                INSERT INTO pages (
                    url, title, status_code, depth, links, response_time, success, error
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(url) DO UPDATE SET
                    title = excluded.title,
                    status_code = excluded.status_code,
                    depth = excluded.depth,
                    links = excluded.links,
                    response_time = excluded.response_time,
                    success = excluded.success,
                    error = excluded.error,
                    created_at = CURRENT_TIMESTAMP
                """,
                [
                    (
                        page.url,
                        page.title,
                        page.status_code,
                        page.depth,
                        json.dumps(page.links),
                        page.response_time,
                        int(page.success),
                        page.error,
                    )
                    for page in pages
                ],
            )

    def get_pages(self) -> list[PageRecord]:
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT url, title, status_code, depth, links, response_time, success, error
                FROM pages
                ORDER BY id
                """
            ).fetchall()

        return [
            PageRecord(
                url=row["url"],
                title=row["title"],
                status_code=row["status_code"],
                depth=row["depth"],
                links=json.loads(row["links"]),
                response_time=row["response_time"],
                success=bool(row["success"]),
                error=row["error"],
            )
            for row in rows
        ]

    def get_stats(self) -> StatsResponse:
        pages = self.get_pages()
        total_pages = len(pages)
        total_links = sum(len(page.links) for page in pages)
        failed_requests = sum(1 for page in pages if not page.success)
        average_response_time = (
            sum(page.response_time for page in pages) / total_pages if total_pages else 0.0
        )

        return StatsResponse(
            total_pages_crawled=total_pages,
            total_links_found=total_links,
            failed_requests=failed_requests,
            average_response_time=average_response_time,
        )

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.path)
        connection.row_factory = sqlite3.Row
        return connection


database = Database()


def get_database() -> Database:
    return database
