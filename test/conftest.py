import pytest
from fake_database import user
from app.services.user import UserService


@pytest.fixture
def user_data():
    print("\nInitializing database")
    print("Getting Users Data")

    return user.users_info, user.users_role, user.users_profile


@pytest.fixture
def user_service(user_data):
    user_service = UserService(*user_data)
    return user_service

