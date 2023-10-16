from typing import Generator

from src.db.engine import SessionLocal


def get_session() -> Generator:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
