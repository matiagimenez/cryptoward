from datetime import datetime
from typing import Any
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class CurrencyPrice(SQLModel, table=True):  # type: ignore[call-arg]
    id_: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        schema_extra={
            "validation_alias": "id",
            "serialization_alias": "id",
        },
    )
    currency: str
    price: str
    timestamp: float
    created_dt: datetime = Field(default=None)

    def model_post_init(self, __context: Any) -> None:
        self.created_dt = datetime.fromtimestamp(self.timestamp)
