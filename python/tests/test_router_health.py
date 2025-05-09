from pathlib import Path
import sys

PARENT_PATH = Path(__file__).resolve().parent.parent

sys.path.append(f"{PARENT_PATH}")
sys.path.append(f"{PARENT_PATH}/src")


from fastapi.testclient import TestClient
from src.routers.router_health import router


client = TestClient(router)


def test_get_health_success():
    response = client.get("/health")
    assert response.status_code == 200
    assert "system" in response.json()
    assert "processor" in response.json()
    assert "architecture" in response.json()
    assert "release" in response.json()
    assert "version" in response.json()
    assert "machine" in response.json()
    assert "memory" in response.json()
    assert "cpu" in response.json()
    assert "disk" in response.json()
