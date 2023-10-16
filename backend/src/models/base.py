import uuid
from datetime import datetime

from pydantic import UUID4
from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column

from pydantic.alias_generators import to_snake


class DbBase(DeclarativeBase):
    id: Mapped[UUID4] = mapped_column(primary_key=True, default=uuid.uuid4)
    # __name__: str
    # __table__: Table
    # metadata: Any
    # registry: Any

    # Generate __tablename__ automatically
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return to_snake(cls.__name__)


class AuditMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now
    )
    # __name__: str


# Import all the models, so that DbBase has them before being
# imported by Alembic
# ruff: noqa
from src.models.todos import Todo
