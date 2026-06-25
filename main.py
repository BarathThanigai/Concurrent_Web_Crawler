from dataclasses import asdict

from fastapi import Depends, FastAPI, HTTPException

from crawler import ConcurrentCrawler
from database import Database, get_database
from models import CrawlRequest, CrawlResponse, PageRecord, StatsResponse

app = FastAPI(title="Concurrent Web Crawler")


@app.on_event("startup")
def startup() -> None:
    get_database().initialize()


@app.post("/crawl", response_model=CrawlResponse)
async def crawl(request: CrawlRequest, db: Database = Depends(get_database)) -> CrawlResponse:
    try:
        crawler = ConcurrentCrawler(
            seed_url=str(request.seed_url),
            max_depth=request.max_depth,
            max_concurrency=request.max_concurrency,
        )
        pages = await crawler.crawl()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Crawler failed unexpectedly") from exc

    db.save_pages(pages)
    page_records = [PageRecord(**asdict(page)) for page in pages]
    return CrawlResponse(crawled_pages=len(page_records), pages=page_records)


@app.get("/pages", response_model=list[PageRecord])
def pages(db: Database = Depends(get_database)) -> list[PageRecord]:
    return db.get_pages()


@app.get("/stats", response_model=StatsResponse)
def stats(db: Database = Depends(get_database)) -> StatsResponse:
    return db.get_stats()
