from fastapi import APIRouter
from app.config import settings


router = APIRouter()


@router.get("", include_in_schema=False)
async def healthcheck():
    response = {
        "status": "ok",
        "version": "settings.APP_VERSION",
    }
    return response
