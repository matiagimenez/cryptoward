import pytest


@pytest.fixture(scope="module", autouse=True)
def vcr_config() -> dict[str, str]:
    return {"record_mode": "once"}
