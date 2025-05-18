from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Event(BaseModel):
    id_: UUID = Field(alias="id", default_factory=uuid4)
    currency: str
    price: str | None
    timestamp: float = Field(default=datetime.now().timestamp())
