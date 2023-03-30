import pytest
from fake_database.user import users_profile, users_role, users_info
from app.services.user import UserService
# from .user_fixtures import user_data


@pytest.mark.asyncio
async def test_delete_user_works_properly(user_data, user_service):
    # user_service = UserService(users_info, users_role, users_profile)
    # print(*user_data)
    # user_service = UserService(*user_data)
    user_to_delete = 2
    await user_service.delete_user_by_id(user_to_delete)
    assert user_to_delete not in users_info
    assert user_to_delete not in users_profile
    assert user_to_delete not in users_role
