from fastapi import APIRouter

from app.health.api import router as health_router
from app.data.api import router as data_router

api_router = APIRouter()
api_router.include_router(health_router, prefix="/healthcheck")

api_v1_router = APIRouter(prefix="/v1")
api_v1_router.include_router(data_router, prefix="/data")

api_router.include_router(api_v1_router, prefix="/api")