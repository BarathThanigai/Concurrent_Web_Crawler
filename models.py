from pydantic import AnyHttpUrl, BaseModel, Field


class CrawlRequest(BaseModel):
    seed_url: AnyHttpUrl
    max_depth: int = Field(ge=0, le=10)
    max_concurrency: int = Field(ge=1, le=100)


class PageRecord(BaseModel):
    url: str
    title: str
    status_code: int | None
    depth: int
    links: list[str]
    response_time: float
    success: bool
    error: str | None = None


class CrawlResponse(BaseModel):
    crawled_pages: int
    pages: list[PageRecord]


class StatsResponse(BaseModel):
    total_pages_crawled: int
    total_links_found: int
    failed_requests: int
    average_response_time: float
