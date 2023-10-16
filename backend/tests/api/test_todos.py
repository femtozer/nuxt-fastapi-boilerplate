from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.core.config import settings
from tests.utils.todos import create_random_todo, get_random_todo

DATASOURCES_URL = f"{settings.API_PREFIX}/todos"
FAKE_BEARER = {"Authorization": "Bearer fakefakefake"}


def test_create_todo(client: TestClient, session: Session) -> None:
    todo = get_random_todo()
    response = client.post(
        DATASOURCES_URL,
        headers=FAKE_BEARER,
        json=jsonable_encoder(todo),
    )
    assert response.status_code == 200
    content = response.json()
    assert content.get("title") == todo.title


def test_get_todo(client: TestClient, session: Session) -> None:
    todo = create_random_todo(session)
    response = client.get(
        f"{DATASOURCES_URL}/{todo.id}",
        headers=FAKE_BEARER,
    )
    assert response.status_code == 200
    content = response.json()
    assert content.get("title") == todo.title


def test_get_todos(client: TestClient, session: Session) -> None:
    todo = create_random_todo(session)
    response = client.get(
        f"{DATASOURCES_URL}",
        headers=FAKE_BEARER,
    )
    assert response.status_code == 200

    content = response.json()
    assert content.get("total") == 1

    items = content.get("items")
    assert len(items) == 1
    assert items[0].get("title") == todo.title


def test_update_todo(client: TestClient, session: Session) -> None:
    todo = create_random_todo(session)
    todo.title = "updated"
    response = client.put(
        f"{DATASOURCES_URL}/{todo.id}",
        headers=FAKE_BEARER,
        json=jsonable_encoder(todo),
    )
    assert response.status_code == 200
    content = response.json()
    assert content.get("title") == todo.title


def test_delete_todo(client: TestClient, session: Session) -> None:
    todo = create_random_todo(session)
    response = client.delete(
        f"{DATASOURCES_URL}/{todo.id}",
        headers=FAKE_BEARER,
    )
    assert response.status_code == 204

    response = client.get(
        f"{DATASOURCES_URL}/{todo.id}",
        headers=FAKE_BEARER,
    )
    assert response.status_code == 404
