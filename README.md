# Concurrent Web Crawler

A FastAPI backend that crawls internal links concurrently with `asyncio`, `aiohttp`, BeautifulSoup, and SQLite.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

Open the interactive API docs at:

```text
http://127.0.0.1:8000/docs
```

## API Usage

### Welcome

```http
GET /
```

Returns a welcome message and the main available endpoints.

### Start a Crawl

```http
POST /crawl
Content-Type: application/json

{
  "seed_url": "https://example.com",
  "max_depth": 2,
  "max_concurrency": 10
}
```

Limits:

- `max_depth`: 0 to 3
- `max_concurrency`: 1 to 20

The response is a clean crawl summary:

```json
{
  "job_id": "2f5b8cc8-0f2b-4f2d-a514-6566b4dfc9e7",
  "crawled_pages": 4,
  "total_links_found": 12,
  "failed_requests": 0,
  "message": "Crawl completed. Full results are available at /crawl/2f5b8cc8-0f2b-4f2d-a514-6566b4dfc9e7."
}
```

### Get Crawl Details

```http
GET /crawl/{job_id}
```

Returns metadata for one crawl job and all page details captured for that job.

### Get All Stored Pages

```http
GET /pages
```

Returns all stored crawled page records across crawl jobs.

### Get Stats

```http
GET /stats
```

Returns total pages crawled, total links found, failed requests, and average response time.

## Architecture

- `main.py`: FastAPI app, request handling, endpoint definitions.
- `crawler.py`: Concurrent BFS crawler, robots.txt checks, timeout handling, link extraction.
- `database.py`: SQLite schema, crawl job storage, page storage, query helpers.
- `models.py`: Pydantic request and response models.

The crawler processes pages one depth layer at a time to preserve BFS-style traversal. It uses a visited set to avoid duplicate URLs, checks `robots.txt` before fetching pages, respects `max_depth`, and limits active HTTP requests with an asyncio semaphore.


- FastAPI Swagger docs at `/docs`
- `POST /crawl` summary response
- `GET /crawl/{job_id}` full crawl details
- `GET /stats` aggregate statistics
