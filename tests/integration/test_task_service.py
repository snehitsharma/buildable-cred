from fastapi.testclient import TestClient

from main import app
from services import tasks as task_service


def setup_function():
    task_service._tasks.clear()
    task_service._next_id = 1


def test_task_api_crud_lifecycle():
	with TestClient(app) as client:
		response = client.post(
			"/tasks/",
			json={"title": "buy milk", "description": "2%"},
		)

		assert response.status_code == 200
		assert response.json() == {
			"id": 1,
			"title": "buy milk",
			"description": "2%",
			"completed": False,
		}

		assert client.get("/tasks/").json() == [response.json()]
		assert client.get("/tasks/1").json() == response.json()

		response = client.put(
			"/tasks/1",
			json={"title": "buy oat milk", "completed": True},
		)

		assert response.status_code == 200
		assert response.json() == {
			"id": 1,
			"title": "buy oat milk",
			"description": None,
			"completed": True,
		}

		response = client.delete("/tasks/1")

		assert response.status_code == 200
		assert response.json() is True
		assert client.get("/tasks/").json() == []


def test_task_api_rejects_invalid_payload():
	with TestClient(app) as client:
		response = client.post("/tasks/", json={"description": "missing title"})

	assert response.status_code == 422
