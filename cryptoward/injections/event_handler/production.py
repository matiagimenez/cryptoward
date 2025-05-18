import inject

from cryptoward.event_handler import EventHandler, KafkaEventHandler


def production_event_handler_injector(binder: inject.Binder) -> None:
    binder.bind(EventHandler, KafkaEventHandler())
