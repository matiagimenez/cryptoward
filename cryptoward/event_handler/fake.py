from mockafka import FakeAdminClientImpl, FakeProducer
from mockafka.admin_client import NewTopic

from cryptoward.logging import log
from cryptoward.settings import Settings

from .base import EventHandler
from .schemas import Event


class FakeEventHandler(EventHandler):
    def __init__(self) -> None:
        FakeAdminClientImpl().create_topics([
            NewTopic(topic=Settings.KAFKA_TOPIC, num_partitions=1, replication_factor=1)
        ])

    @property
    def producer(self) -> FakeProducer:
        return FakeProducer()

    def send_event(self, event: Event) -> None:
        event_dict = event.model_dump(mode="json", by_alias=True)
        self.producer.produce(Settings.KAFKA_TOPIC, event_dict, partition=0)
        log(f"Event sent to broker: {event_dict}")
