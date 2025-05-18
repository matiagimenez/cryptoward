from unittest.mock import Mock

from cryptoward.event_handler import Event, EventHandler


def test_send_event(
    event_handler: EventHandler, event: Event, kafka_producer: Mock
) -> None:
    event_handler.send_event(event)
    assert kafka_producer.send.call_count == 1
    assert kafka_producer.flush.call_count == 1
    assert kafka_producer.send.call_args[0][0] == event_handler.topic
