from loguru import logger
from .config import settings
from pathlib import Path

dir_path = Path.joinpath(settings.root_dir, "logs")
file_paths = [Path.joinpath(dir_path, "app.log"), Path.joinpath(dir_path, "error.log")]

dir_path.mkdir(parents=True, exist_ok=True)


for file_path in file_paths:
    if not file_path.exists():
        file_path.touch()


logger.add(file_paths[0], format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")

logger.add(
    file_paths[1],
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
    level="ERROR",
)


class Logger:
    @classmethod
    def info(cls, message) -> None:
        logger.info(message)

    @classmethod
    def error(cls, message) -> None:
        logger.error(message)
