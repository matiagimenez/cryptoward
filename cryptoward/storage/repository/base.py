from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Any, Generic, TypeVar, get_args
from uuid import UUID

from sqlmodel import SQLModel

T = TypeVar("T", bound=SQLModel)


class StorageRepository(ABC, Generic[T]):
    @property
    def entity(self) -> type[T]:
        return get_args(self.__orig_class__)[0]  # type: ignore[no-any-return, attr-defined] # pylint: disable=no-member

    @abstractmethod
    def add(self, entity: T) -> T: ...

    @abstractmethod
    def delete_all(self) -> None: ...

    @abstractmethod
    def get_by_id(self, id_: UUID) -> T | None: ...

    @abstractmethod
    def get_all(self) -> Iterable[T]: ...

    @abstractmethod
    def get_by_params(self, params: dict[str, Any]) -> Iterable[T]: ...
