import enum
from typing import Optional

from src.schemas.base import AppBase, ReadBase


class TodoPriority(str, enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class TodoBase(AppBase):
    title: str
    description: Optional[str]
    priority: TodoPriority


class TodoRead(ReadBase, TodoBase):
    pass


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    pass
