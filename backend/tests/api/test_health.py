from fastapi.testclient import TestClient

from src.core.config import settings


def test_get_health(client: TestClient) -> None:
    r = client.get(f"{settings.API_PREFIX}/health")

    assert r.status_code == 200
    assert r.json().get("status") == "OK"
