from collections.abc import Generator

from cryptoward.utils import Level, log


def test_log(
    capture_logs: Generator[list[str], None, None], log_level: Level, message: str
) -> None:
    log(message, log_level)
    logs = list(capture_logs)
    assert message in logs[0]
    assert log_level.value in logs[0]
