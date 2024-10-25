from fastapi import APIRouter

from app.services.data_loader.data_loader import NetCDFDataLoader
from app.config import settings

router = APIRouter()


@router.get("")
async def get_data():
    print("Loading Data ...")
    file_path = settings.DATA_PATH
    print("File Path ", file_path)
    loader = NetCDFDataLoader(file_path=file_path)
    data = loader.load()
    loader.read_head()