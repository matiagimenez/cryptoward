from abc import ABC, abstractmethod

from .schemas import Event


class EventHandler(ABC):
    @abstractmethod
    def send_event(self, event: Event) -> None:
        exception = "Subclasses must implement this method."
        raise NotImplementedError(exception)
