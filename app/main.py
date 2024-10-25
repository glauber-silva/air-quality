import uvicorn

from fastapi import FastAPI

from app.config import settings
from app.api import api_router


app = FastAPI(
    title="Air Quality",
    description="A RESTful API that interacts with air quality data and handles basic filtering and analytics",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/",
    redoc_url="/docs"
)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True,
    )