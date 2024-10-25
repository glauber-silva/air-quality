from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    APP_VERSION: str
    APP_NAME: str
    DATA_FILE: str = "pm2-5-netcdf.nc"
    DATA_PATH: str = str(Path(__file__).resolve().parent.parent / 'contrib' / DATA_FILE)

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()