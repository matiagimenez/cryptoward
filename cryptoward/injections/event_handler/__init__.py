import inject

from cryptoward.injections import Environment

from .production import production_event_handler_injector
from .test import test_event_handler_injector

injectors = {
    Environment.TEST: test_event_handler_injector,
    Environment.PRODUCTION: production_event_handler_injector,
}


def configure_event_handler(environment: Environment) -> None:
    inject.clear_and_configure(injectors[environment])


__all__ = ["configure_event_handler"]
