from collections.abc import Generator
from unittest.mock import Mock

import pytest
from kafka import KafkaProducer
from polyfactory.factories.pydantic_factory import ModelFactory
from polyfactory.pytest_plugin import register_fixture
from pytest_mock import MockerFixture

from cryptoward.event_handler import Event, EventHandler, KafkaEventHandler
from cryptoward.settings import Settings


@register_fixture(name="event_factory")
class EventFactory(ModelFactory[Event]): ...


@pytest.fixture
def event(event_factory: ModelFactory[Event]) -> Event:
    return event_factory.build()


@pytest.fixture
def event_handler() -> EventHandler:
    return KafkaEventHandler()


@pytest.fixture
def kafka_producer(mocker: MockerFixture) -> Generator[Mock, None, None]:
    producer = mocker.Mock(spec=KafkaProducer)
    mocker.patch("cryptoward.event_handler.kafka.KafkaProducer", return_value=producer)
    return producer  # type: ignore[no-any-return]


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
