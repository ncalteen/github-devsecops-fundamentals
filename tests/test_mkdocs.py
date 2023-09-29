import subprocess
import time

import pytest
import requests


@pytest.fixture(scope="session", autouse=True)
def start_mkdocs_server():
    # Start the server in a subprocess.
    server = subprocess.Popen(["mkdocs", "serve"])

    # Give the server a second to start up.
    time.sleep(1)

    yield server

    # After the tests are done, kill the server.
    server.kill()


def test_mkdocs_static_page():
    response = requests.get("http://localhost:8000")

    assert response.status_code == 200
    assert "GitHub DevSecOps Fundamentals" in response.text
