from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_crud_flow():
    r = client.post("/api/v1/todos", json={"title": "Comprar pão"})
    assert r.status_code == 201
    todo = r.json()
    todo_id = todo["id"]
    assert todo["title"] == "Comprar pão"
    assert todo["completed"] is False

    r = client.get(f"/api/v1/todos/{todo_id}")
    assert r.status_code == 200

    r = client.patch(f"/api/v1/todos/{todo_id}", json={"completed": True})
    assert r.status_code == 200
    assert r.json()["completed"] is True

    r = client.get("/api/v1/todos?limit=10")
    assert r.status_code == 200
    assert any(t["id"] == todo_id for t in r.json())

    r = client.delete(f"/api/v1/todos/{todo_id}")
    assert r.status_code == 204

    r = client.get(f"/api/v1/todos/{todo_id}")
    assert r.status_code == 404