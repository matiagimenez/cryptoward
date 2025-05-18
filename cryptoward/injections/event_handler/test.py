import inject

from cryptoward.event_handler import EventHandler, FakeEventHandler


def test_event_handler_injector(binder: inject.Binder) -> None:
    binder.bind(EventHandler, FakeEventHandler())
