from pathlib import Path
import sys

PARENT_PATH = Path(__file__).resolve().parent.parent

sys.path.append(f"{PARENT_PATH}")
sys.path.append(f"{PARENT_PATH}/src")

from fastapi.testclient import TestClient
from requests import patch
from src.routers.router_github import router
import pytest

client = TestClient(router)


def test_get_github_status_success():
    response = client.get("/github-status")
    assert response.status_code == 200
    assert "message" not in response.json()


def test_get_github_status_failure():
    # Mocking the requests library to simulate a failed request
    with pytest.raises(Exception):
        with patch("src.routers.router_github.requests.get") as mock_get:
            mock_get.side_effect = Exception("Mocked exception")
            response = client.get("/github-status")
            assert response.status_code == 500
            assert "Failed to get GitHub status" in response.json()["message"]
