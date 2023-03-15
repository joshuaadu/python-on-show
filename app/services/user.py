from typing import Optional
from app.schemas.user import (
    FullUserProfile,
    Profile,
    User
)

users_info = {
    0: {
        "name": "Joe Men",
        "age": 20
    },
    1: {
        "name": "Roe Ken",
        "age": 20
    },
    2: {
        "name": "Betty Lov",
        "age": 20
    },
}

users_role = {
    0: {
        "name": "developer lead",
        "id": 1,
        "description": "PaySwitch developer lead"
    },
    1: {
        "name": "UI developer",
        "id": 1,
        "description": "PaySwitch UI developer"
    },
    2: {
        "name": "Mobile developer",
        "id": 1,
        "description": "PaySwitch Mobile developer"
    }

}

users_profile = {
    0: {
        "title": "Software Developer",
        "description": "PaySwitch software developer",
        "address": "accra",
        "roles": []
    },
    1: {
        "title": "Software Developer",
        "description": "PaySwitch software developer",
        "address": "Koforidua",
        "roles": []
    },
    2: {
        "title": "Software Developer",
        "description": "PaySwitch software developer",
        "address": "Tema",
        "roles": []
    },
}


class UserService:
    def __init__(self):
        pass

    async def get_users_with_pagination(self, start: int, limit: int) -> (list[FullUserProfile], int):
        keys = list(users_info.keys())
        keys_length = len(keys)
        users = []
        for index in range(0, keys_length):
            if index < start:
                continue
            if len(users) >= limit:
                break
            users.append(await self.get_user_info(keys[index]))
        return users, keys_length

    @staticmethod
    async def get_user_info(user_id: int = 0) -> FullUserProfile:
        user_profile = Profile(**users_profile[user_id])
        user_info = User(**users_info[user_id])
        full_user_profile = {
            **user_info.dict(),
            **user_profile.dict(),
            "department": "Tech"
        }

        full_user_profile = FullUserProfile(**full_user_profile)
        return full_user_profile

    @staticmethod
    async def create_update_user(full_user_profile: FullUserProfile, user_id: Optional[int] = None) -> int:
        """
        Create user and new unique user id if not exist otherwise update the user
        Placeholder implementation later to be updated with DB

        :param full_user_profile: FullUserProfile - User information saved in database
        :param user_id: Optional[int] - user_id if already exists, otherwise to be set
        :return: user_id: int - existing or new user id
        """
        if user_id is None:
            user_id = len(users_info)

        users_info[user_id] = {
            "name": full_user_profile.name,
            "age": full_user_profile.age
        }
        users_profile[user_id] = {
            "title": full_user_profile.title,
            "description": full_user_profile.description,
            "address": full_user_profile.address,
            "roles": [role.dict() for role in full_user_profile.roles]
        }
        users_role[user_id] = [role.dict() for role in full_user_profile.roles]

        return user_id

    @staticmethod
    async def delete_user_by_id(user_id: int) -> str:
        global users_info
        global users_role
        global users_profile

        del users_info[user_id]
        del users_profile[user_id]
        del users_role[user_id]
        return "Success!"
