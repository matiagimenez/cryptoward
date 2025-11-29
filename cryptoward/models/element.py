from pydantic import BaseModel, Field


class Element(BaseModel):
    tag: str
    data_attributes: dict[str, str] = Field(default_factory=dict)
