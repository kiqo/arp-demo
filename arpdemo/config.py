from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Recipe image & OCR upload"
    data_folder: Path = Path("/data/")

    class Config:
        env_file = ".env"


settings = Settings()
