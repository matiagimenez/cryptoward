from kafka import KafkaProducer

from cryptoward.logging import log
from cryptoward.settings import Settings

from .base import EventHandler
from .schemas import Event


class KafkaEventHandler(EventHandler):
    @property
    def producer(self) -> KafkaProducer:
        return KafkaProducer(
            bootstrap_servers=[Settings.KAFKA_HOST],
            value_serializer=lambda v: str(v).encode("utf-8"),
        )

    def send_event(self, event: Event) -> None:
        event_dict = event.model_dump(mode="json", by_alias=True)
        self.producer.send(Settings.KAFKA_TOPIC, event_dict)
        self.producer.flush()
        log(f"Event sent to broker: {event_dict}")
