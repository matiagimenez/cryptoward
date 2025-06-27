from pathlib import Path

import pytest

from cryptoward.injections import Environment, configure_injections

pytest_plugins = ["tests.conftest_settings", "tests.conftest_polyfactory"]


@pytest.fixture(autouse=True)
def injection_config() -> None:
    configure_injections(Environment.TEST)


@pytest.fixture(scope="module", autouse=True)
def vcr_config() -> dict[str, str]:
    return {"record_mode": "once"}


@pytest.fixture(scope="session", autouse=True)
def cleanup_test_db() -> None:
    db_path = Path("test.db")
    if Path(db_path):
        Path.unlink(db_path)
