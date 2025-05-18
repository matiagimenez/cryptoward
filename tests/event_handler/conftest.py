from collections.abc import Generator
from unittest.mock import Mock

import pytest
from kafka import KafkaProducer
from polyfactory.factories.pydantic_factory import ModelFactory
from polyfactory.pytest_plugin import register_fixture
from pytest_mock import MockerFixture

from cryptoward.event_handler import Event, EventHandler, KafkaEventHandler


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
