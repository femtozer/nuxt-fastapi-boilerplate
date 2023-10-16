import logging
from typing import Any, Dict, Generic, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import UUID4, BaseModel
from pydantic.alias_generators import to_snake
from sqlalchemy import UnaryExpression, asc, case, desc
from sqlalchemy.orm import Query, Session

from src.models.base import DbBase
from src.schemas.base import Page

ModelType = TypeVar("ModelType", bound=DbBase)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(
        self,
        model: Type[ModelType],
    ):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, session: Session, id: UUID4) -> ModelType | None:
        q = session.query(self.model).filter(self.model.id == id)

        return q.first()

    def get_nb_rows(self, session: Session) -> int:
        return session.query(self.model).count()

    def get_multi(
        self,
        session: Session,
        *,
        skip: int | None = None,
        limit: int | None = None,
        sort: str | None = None,
        is_desc: bool = False,
    ) -> Page[ModelType]:
        q = session.query(self.model)

        return self.order_and_paginate_results(
            q,
            skip=skip,
            limit=limit,
            sort=sort,
            is_desc=is_desc,
        )

    def create(
        self,
        session: Session,
        *,
        obj_in: CreateSchemaType,
        user_upn: str | None = None,
    ) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in, by_alias=False)
        if user_upn:
            obj_in_data["created_by"] = user_upn
            obj_in_data["updated_by"] = user_upn

        session_obj = self.model(**obj_in_data)
        session.add(session_obj)
        session.commit()
        session.refresh(session_obj)
        return session_obj

    def update(
        self,
        session: Session,
        *,
        session_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]],
    ) -> ModelType:
        obj_fields = [o.name for o in session_obj.__table__.columns]
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)

        for field in obj_fields:
            if field in update_data:
                setattr(session_obj, field, update_data[field])
        session.add(session_obj)
        session.commit()
        session.refresh(session_obj)
        return session_obj

    def remove(self, session: Session, *, id: UUID4) -> None:
        obj = session.get(self.model, id)
        session.delete(obj)
        session.commit()

    def order_and_paginate_results(
        self,
        q: Query,
        *,
        skip: int | None = None,
        limit: int | None = None,
        sort: str | None = None,
        is_desc: bool = False,
    ) -> Page[ModelType]:
        if sort:
            sort = to_snake(sort)
            try:
                sort_attr = getattr(self.model, sort)
                if sort_attr.type.python_type == str:
                    order_by: UnaryExpression = (
                        desc(case((sort_attr.is_(None), ""), else_=sort_attr))
                        if is_desc
                        else asc(case((sort_attr.is_(None), ""), else_=sort_attr))
                    )
                else:
                    order_by = desc(sort_attr) if is_desc else asc(sort_attr)
                q = q.order_by(order_by)
            except AttributeError as e:
                logging.exception(e)
        if skip is not None and limit is not None:
            total = q.count()
            items = q.offset(skip).limit(limit).all()
        else:
            items = q.all()
            total = len(items)

        return Page(items=items, total=total)
