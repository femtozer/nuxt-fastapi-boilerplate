from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from src.db.engine import engine
from src.models.base import DbBase


@pytest.fixture(scope="session")
def db_engine() -> Generator:
    DbBase.metadata.drop_all(engine)
    DbBase.metadata.create_all(engine)

    yield engine

    DbBase.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def session(db_engine: Engine) -> Generator:
    connection = engine.connect()

    # begin a non-ORM transaction
    connection.begin()

    # bind an individual Session to the connection
    session = Session(bind=connection)
    # db = Session(db_engine)

    yield session

    session.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(session: Session) -> Generator:
    from src.api.deps import get_session
    from src.main import app

    app.dependency_overrides[get_session] = lambda: session
    with TestClient(app) as c:
        yield c
