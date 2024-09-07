from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings

ROOT_DIR = Path(__file__).parent.parent.parent


class Settings(BaseSettings):
    spreadsheet_key: str = Field(alias="SPREADSHEET_KEY", default="")
    root_dir: Path = ROOT_DIR


settings = Settings()
