from .config import Environment
from .event_handler import configure_event_handler


def configure_injections(environment: Environment) -> None:
    configure_event_handler(environment)
