from typing import Optional
from app.schemas.user import (
    FullUserProfile,
    Profile,
    User
)
from app.exceptions import UserNotFound


class UserService:
    def __init__(self, users_info: dict, users_role: dict, users_profile: dict):
        self.users_info = users_info
        self.users_role = users_role
        self.users_profile = users_profile
        pass

    async def get_users_with_pagination(self, start: int, limit: int) -> (list[FullUserProfile], int):
        keys = list(self.users_info.keys())
        keys_length = len(keys)
        users = []
        for index in range(0, keys_length):
            if index < start:
                continue
            if len(users) >= limit:
                break
            users.append(await self.get_user_info(keys[index]))
        return users, keys_length

    async def get_user_info(self, user_id: int = 0) -> FullUserProfile:
        if user_id not in self.users_info:
            raise UserNotFound(user_id=user_id)
        user_profile = Profile(**self.users_profile[user_id])
        user_info = User(**self.users_info[user_id])
        full_user_profile = {
            **user_info.dict(),
            **user_profile.dict(),
            "department": "Tech"
        }

        full_user_profile = FullUserProfile(**full_user_profile)
        return full_user_profile

    async def create_update_user(self, full_user_profile: FullUserProfile, user_id: Optional[int] = None) -> int:
        """
        Create user and new unique user id if not exist otherwise update the user
        Placeholder implementation later to be updated with DB

        :param full_user_profile: FullUserProfile - User information saved in database
        :param user_id: Optional[int] - user_id if already exists, otherwise to be set
        :return: user_id: int - existing or new user id
        """
        if user_id is None:
            user_id = len(self.users_info)

        self.users_info[user_id] = {
            "name": full_user_profile.name,
            "age": full_user_profile.age
        }
        self.users_profile[user_id] = {
            "title": full_user_profile.title,
            "description": full_user_profile.description,
            "address": full_user_profile.address,
            "roles": [role.dict() for role in full_user_profile.roles]
        }
        self.users_role[user_id] = [role.dict() for role in full_user_profile.roles]

        return user_id

    async def delete_user_by_id(self, user_id: int) -> str:
        if user_id not in self.users_info:
            raise UserNotFound(user_id=user_id)
        try:
            del self.users_info[user_id]
            del self.users_profile[user_id]
            del self.users_role[user_id]
        except Exception:
            print("Failed to delete")
        return "Success!"
