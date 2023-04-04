import pytest
from fake_database import user
from app.services.user import UserService
from app.schemas.user import FullUserProfile


@pytest.fixture
def user_data():
    print("\nInitializing database")
    print("Getting Users Data")

    return user.users_info, user.users_role, user.users_profile


@pytest.fixture
def user_service(user_data):
    user_service = UserService(*user_data)
    return user_service


@pytest.fixture(scope="session")
def valid_user_id() -> int:
    return 0


@pytest.fixture(scope="session")
def invalid_user_id() -> int:
    return 4


@pytest.fixture
def testing_rate_limit() -> int:
    return 15


@pytest.fixture()
def new_user() -> FullUserProfile:
    return FullUserProfile(title="string",
                           description="string",
                           address="string",
                           roles=[
                               {
                                   "name": "string",
                                   "id": 0,
                                   "description": "string"
                               }
                           ],
                           department="mdkdkdkdkdkd",
                           name="string",
                           age=19,
                           )


@pytest.fixture()
def updated_user() -> FullUserProfile:
    return FullUserProfile(title="Update",
                           description="string",
                           address="string",
                           roles=[
                               {
                                   "name": "string",
                                   "id": 0,
                                   "description": "string"
                               }
                           ],
                           department="mdkdkdkdkdkd",
                           name="string",
                           age=20,
                           )
