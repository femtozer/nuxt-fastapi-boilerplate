from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import AuditMixin, DbBase


class Todo(DbBase, AuditMixin):
    """Todo DB table"""

    title: Mapped[str] = mapped_column(index=True)
    description: Mapped[str] = mapped_column(nullable=True)
    priority: Mapped[str]
