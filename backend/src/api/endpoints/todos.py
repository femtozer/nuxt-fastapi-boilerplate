import logging
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from pydantic import UUID4
from sqlalchemy.orm import Session

from src import crud
from src.api.deps import get_session
from src.core.config import settings
from src.models.todos import Todo
from src.schemas.base import Page
from src.schemas.todos import TodoCreate, TodoRead, TodoUpdate

router = APIRouter()


@router.get(
    "",
    response_model=Page[TodoRead],
)
def read_todos(
    *,
    session: Session = Depends(get_session),
    skip: Optional[int] = Query(0, ge=0),
    limit: Optional[int] = Query(None, ge=1, le=settings.MAX_PAGE_SIZE),
    sort: Optional[str] = None,
    is_desc: bool = False,
) -> Page[Todo]:
    """
    Retrieve todos.
    """
    try:
        todos = crud.todos.get_multi(session, skip=skip, limit=limit, sort=sort, is_desc=is_desc)
        return todos
    except (AttributeError, KeyError, ValueError) as e:
        logging.exception(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        ) from e
    except Exception as e:
        logging.exception(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong",
        ) from e


@router.post(
    "",
    response_model=TodoRead,
)
def create_todo(
    *,
    session: Session = Depends(get_session),
    todo_in: TodoCreate,
) -> Todo:
    """
    Create a todo.
    """
    try:
        todo = crud.todos.create(session=session, obj_in=todo_in)
    except Exception as e:
        logging.exception(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not create todo",
        ) from e
    return todo


@router.put(
    "/{_id}",
    response_model=TodoRead,
)
def update_todo(
    *,
    session: Session = Depends(get_session),
    _id: UUID4,
    todo_in: TodoUpdate,
) -> Todo:
    """
    Update a todo.
    """
    todo = crud.todos.get(session=session, id=_id)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

    try:
        todo = crud.todos.update(session=session, session_obj=todo, obj_in=todo_in)
    except Exception as e:
        logging.exception(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not update todo",
        ) from e
    return todo


@router.get(
    "/{_id}",
    response_model=TodoRead,
)
def read_todo(
    *,
    session: Session = Depends(get_session),
    _id: UUID4,
) -> Todo:
    """
    Get todo by ID.
    """
    todo = crud.todos.get(session=session, id=_id)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return todo


@router.delete("/{_id}", status_code=204, response_class=Response)
def delete_todo(
    *,
    session: Session = Depends(get_session),
    _id: UUID4,
) -> None:
    """
    Delete a todo.
    """
    todo = crud.todos.get(session=session, id=_id)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

    try:
        crud.todos.remove(session=session, id=_id)
    except Exception as e:
        logging.exception(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not delete todo",
        ) from e
