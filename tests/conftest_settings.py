from collections.abc import Generator

import pytest

from cryptoward.settings import Settings


@pytest.fixture(autouse=True)
def _patch_kafka_topic() -> Generator[None, None, None]:
    old_value = Settings.KAFKA_TOPIC
    Settings.KAFKA_TOPIC = "test_topic"
    yield
    Settings.KAFKA_TOPIC = old_value


@pytest.fixture(autouse=True)
def _patch_kafka_host() -> Generator[None, None, None]:
    old_value = Settings.KAFKA_HOST
    Settings.KAFKA_HOST = "host"
    yield
    Settings.KAFKA_HOST = old_value
