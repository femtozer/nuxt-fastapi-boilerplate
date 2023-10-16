from src.crud.base import CRUDBase
from src.models.todos import Todo
from src.schemas.todos import TodoCreate, TodoUpdate

todos = CRUDBase[Todo, TodoCreate, TodoUpdate](Todo)
