import pytest

from cryptoward.injections import Environment


@pytest.fixture(params=[Environment.PRODUCTION, Environment.TEST])
def environment(request: pytest.FixtureRequest) -> Environment:
    return request.param  # type: ignore[no-any-return]
