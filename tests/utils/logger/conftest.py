from collections.abc import Generator

import pytest

from cryptoward.utils import Level, get_logger


@pytest.fixture
def capture_logs() -> Generator[list[str]]:
    logger = get_logger()
    output = []
    handler_id = logger.add(output.append)
    yield output
    logger.remove(handler_id)


@pytest.fixture(params=[Level.INFO, Level.WARNING, Level.ERROR, Level.CRITICAL])
def log_level(request: pytest.FixtureRequest) -> Level:
    return request.param  # type: ignore[no-any-return]


@pytest.fixture
def message() -> str:
    return "Test message"
