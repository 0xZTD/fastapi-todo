from todo.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_docs():
    response = client.get("/docs")
    assert response.status_code == 200
