from pydantic import AnyHttpUrl, BaseModel, Field


class CrawlRequest(BaseModel):
    seed_url: AnyHttpUrl
    max_depth: int = Field(ge=0, le=3)
    max_concurrency: int = Field(ge=1, le=20)


class PageRecord(BaseModel):
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


class CrawlResponse(BaseModel):
    job_id: str
    crawled_pages: int
    total_links_found: int
    failed_requests: int
    message: str


class CrawlJobResponse(BaseModel):
    job_id: str
    seed_url: str
    max_depth: int
    max_concurrency: int
    started_at: str
    completed_at: str | None
    pages: list[PageRecord]


class StatsResponse(BaseModel):
    total_pages_crawled: int
    total_links_found: int
    failed_requests: int
    average_response_time: float
    average_response_time_ms: float
