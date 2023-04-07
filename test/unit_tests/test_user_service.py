import pytest
from fake_database.user import users_profile, users_role, users_info
from app.exceptions import UserNotFound


@pytest.mark.asyncio
async def test_delete_user_works_properly(user_data, user_service, valid_user_id):
    # user_service = UserService(users_info, users_role, users_profile)
    # print(*user_data)
    # user_service = UserService(*user_data)
    await user_service.delete_user_by_id(valid_user_id)
    assert valid_user_id not in users_info
    assert valid_user_id not in users_profile
    assert valid_user_id not in users_role


@pytest.mark.asyncio
async def test_delete_invalid_user_raises_proper_exception(user_service, invalid_user_id):
    print(user_service.__dict__)
    with pytest.raises(UserNotFound):
        await user_service.delete_user_by_id(invalid_user_id)
