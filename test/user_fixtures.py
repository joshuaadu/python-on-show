import pytest
from fake_database import user


@pytest.fixture
def user_data():
    return user.users_info, user.users_role, user.users_profile
