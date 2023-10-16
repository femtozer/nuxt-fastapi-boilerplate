import random

from faker import Faker
from sqlalchemy.orm import Session

from src import crud
from src.schemas.todos import TodoCreate, TodoPriority, TodoRead

fake = Faker()


def get_random_todo() -> TodoCreate:
    todo_in = TodoCreate(
        title=fake.catch_phrase(),
        description=fake.paragraph(nb_sentences=3),
        priority=random.choice(list(TodoPriority)),
    )
    return todo_in


def create_random_todo(session: Session) -> TodoRead:
    report_in = get_random_todo()
    report = crud.todos.create(session=session, obj_in=report_in)
    return TodoRead.model_validate(report)
