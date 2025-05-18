import inject

from cryptoward.event_handler import EventHandler, FakeEventHandler, KafkaEventHandler
from cryptoward.injections import Environment, configure_injections


def test_injections_production() -> None:
    configure_injections(Environment.PRODUCTION)
    event_handler = inject.instance(EventHandler)
    assert isinstance(event_handler, KafkaEventHandler)


def test_injections_test() -> None:
    configure_injections(Environment.TEST)
    event_handler = inject.instance(EventHandler)
    assert isinstance(event_handler, FakeEventHandler)
