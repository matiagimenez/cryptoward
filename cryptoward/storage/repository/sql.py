from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any, Generic, TypeVar
from uuid import UUID

from sqlalchemy import BinaryExpression
from sqlmodel import Session, SQLModel, and_, select

from cryptoward.storage.connection import ConnectionFactory

from .base import StorageRepository

T = TypeVar("T", bound=SQLModel)


@dataclass
class SQLStorageRepository(StorageRepository, Generic[T]):
    connection_factory: ConnectionFactory

    @property
    def session(self) -> Session:
        return self.connection_factory.get_session()

    def add(self, entity: T) -> T:
        with self.session as session:
            session.add(entity)
            session.commit()
        return entity

    def get_by_id(self, id_: UUID) -> T | None:
        with self.session as session:
            statement = select(self.entity).where(self.entity.id_ == id_)
            return session.exec(statement).one_or_none()  # type: ignore[no-any-return]

    def get_all(self) -> Iterable[T]:
        with self.session as session:
            statement = select(self.entity)
            return session.exec(statement).all()  # type: ignore[no-any-return]

    def get_by_params(self, params: dict[str, Any]) -> Iterable[T]:
        with self.session as session:
            statement = select(self.entity)
            filters = self._prepare_filters(params)

            if filters:
                statement = statement.where(and_(*filters))

            return session.exec(statement).all()  # type: ignore[no-any-return]

    def _prepare_filters(self, params: dict[str, Any]) -> Iterable[BinaryExpression]:
        filters = []
        for key, value in params.items():
            if not hasattr(self.entity, key):
                exception = f"Model '{self.entity.__name__}' has no attribute '{key}'"
                raise AttributeError(exception)

            filters.append(getattr(self.entity, key) == value)
        return filters
