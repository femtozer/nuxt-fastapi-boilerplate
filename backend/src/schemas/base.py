from datetime import datetime
from typing import Generic, List, TypeVar

from pydantic import UUID4, BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

T = TypeVar("T")


class AppBase(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel, populate_by_name=True, from_attributes=True, use_enum_values=True
    )


class ReadBase(BaseModel):
    id: UUID4


class Page(BaseModel, Generic[T]):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    items: List[T]
    total: int


class AuditBase(BaseModel):
    created_at: datetime
    updated_at: datetime
