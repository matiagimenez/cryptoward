from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    spreadsheet_key: str = Field(alias="SPREADSHEET_KEY", default="")


settings = Settings()
