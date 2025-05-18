import pytest

from cryptoward.injections import Environment, configure_injections

pytest_plugins = ["tests.conftest_settings"]


@pytest.fixture(autouse=True)
def injection_config() -> None:
    configure_injections(Environment.TEST)


@pytest.fixture(scope="module", autouse=True)
def vcr_config() -> dict[str, str]:
    return {"record_mode": "once"}
