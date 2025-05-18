from functools import cached_property

from mockafka import FakeAdminClientImpl, FakeProducer
from mockafka.admin_client import NewTopic

from cryptoward.logging import log
from cryptoward.settings import Settings

from .base import EventHandler
from .schemas import Event


class FakeEventHandler(EventHandler):
    @cached_property
    def admin_client(self) -> FakeAdminClientImpl:
        return FakeAdminClientImpl()

    @cached_property
    def producer(self) -> FakeProducer:
        return FakeProducer()

    @property
    def topic(self) -> str:
        if not self.admin_client.list_topics().topics:
            topic = NewTopic(topic=Settings.KAFKA_TOPIC, num_partitions=1)
            self.admin_client.create_topics([topic])
        return Settings.KAFKA_TOPIC

    def send_event(self, event: Event) -> None:
        event_dict = event.model_dump(mode="json", by_alias=True)
        self.producer.produce(self.topic, event_dict, partition=0)
        log(f"Event sent to broker: {event_dict}")
