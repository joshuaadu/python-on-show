import pytest
from fastapi.testclient import TestClient
from main import create_application


@pytest.fixture(scope="session")
def testing_app() -> TestClient:
    app = create_application()
    testing_app = TestClient(app)
    return testing_app
