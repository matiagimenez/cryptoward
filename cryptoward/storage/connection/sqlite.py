from dataclasses import dataclass

from sqlalchemy.engine import Engine
from sqlmodel import Session, SQLModel, create_engine

from .factory import ConnectionFactory


@dataclass
class SQLiteConnectionFactory(ConnectionFactory):
    database_path: str = "sqlite:///test.db"
    engine: Engine | None = None

    def get_session(self) -> Session:
        return Session(self._get_engine())

    def _get_engine(self) -> Engine:
        if not self.engine:
            self.engine = create_engine(self.database_path, echo=True)
            self._create_tables()
        return self.engine

    def _create_tables(self) -> None:
        assert self.engine
        SQLModel.metadata.create_all(self.engine)
