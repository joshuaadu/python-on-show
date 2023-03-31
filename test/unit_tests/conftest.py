import pytest


@pytest.fixture()
def valid_user_id() -> int:
    return 0


@pytest.fixture()
def invalid_user_id() -> int:
    return 4
