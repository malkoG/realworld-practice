from typing import Dict

from fastapi.testclient import TestClient

from app.core import settings


def test_create_lecture(client: TestClient, random_lecture: Dict[str, str]) -> None:
    response = client.post(f"{settings.API_V1_STR}/lectures", json=random_lecture)
    lecture = response.json()
    assert response.status_code == 200
    assert lecture.get("title") == random_lecture.get("title")
    assert lecture.get("description") == random_lecture.get("description")


def test_read_lectures(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/lectures")
    lectures = response.json()
    assert response.status_code == 200
    assert len(lectures) > 0


def test_update_lecture(client: TestClient, random_lecture: Dict[str, str]) -> None:
    random_lecture["description"] = "Wow"
    response = client.put(f"{settings.API_V1_STR}/lectures", json=random_lecture)
    lecture = response.json()
    assert response.status_code == 200
    assert lecture.get("description") == random_lecture.get("description")


def test_delete_lecture(client: TestClient, random_lecture: Dict[str, str]) -> None:
    response = client.delete(f"{settings.API_V1_STR}/lectures?id={random_lecture.get('id')}")
    message = response.json()
    assert response.status_code == 200
    assert "message" in message
