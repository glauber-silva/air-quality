import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]    
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