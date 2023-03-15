from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Union, Optional

app = FastAPI()


class Role(BaseModel):
    name: str = Field(
        title="Role name",
        description="Current role of the user",
        max_length=20, min_length=5
    )
    id: int
    description: str


class Profile(BaseModel):
    title: str
    description: str
    address: str
    roles: Optional[list[Role]]


class User(BaseModel):
    name: str
    age: int = Field(
        title="Age of User",
        description="The current age of the user",
        gt=18,
        lt=65
    )
    # profile: Profile


class FullUserProfile(User, Profile):
    department_name: str = Field(alias="department")


class MultipleUsersProfile(BaseModel):
    users: list[FullUserProfile]
    total: int


class UserOut(BaseModel):
    user_id: int = Field(title="User ID", description="Id of newly created user")


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


async def get_users_with_pagination(start: int, limit: int) -> (list[FullUserProfile], int):
    keys = list(users_info.keys())
    keys_length = len(keys)
    users = []
    for index in range(0, keys_length):
        if index < start:
            continue
        if len(users) >= limit:
            break
        users.append(await get_user_info(keys[index]))
    return users, keys_length


async def delete_user_by_id(user_id: int):
    global users_info
    global users_role
    global users_profile

    del users_info[user_id]
    del users_profile[user_id]
    del users_role[user_id]
    return "Success!"


@app.get("/", response_class=PlainTextResponse)
async def home():
    return "Hello World from Ghana"


@app.get("/about", response_class=JSONResponse)
async def about():
    return {"name": "John Doe", "address": "East Legon"}


@app.get("/user/me", response_model=FullUserProfile)
async def getuser():
    full_user_profile = await get_user_info()
    return full_user_profile


@app.get("/users/{user_id}", response_model=FullUserProfile)
async def get_user_by_id(user_id: int):
    """
    Endpoint for retrieving a FullUserProfile by the user's unique integer id
    :param user_id:
    :return:
    """
    full_user_profile = await get_user_info(user_id)
    return full_user_profile


@app.get("/users", response_model=MultipleUsersProfile)
async def get_all_users_pagination(start: int = 0, limit: int = 2):
    users, total = await get_users_with_pagination(start, limit)
    users_list = MultipleUsersProfile(users=users, total=total)
    return users_list


@app.post("/users", response_model=UserOut)
async def add_user(full_user_profile: FullUserProfile) -> UserOut:
    new_user = await create_update_user(full_user_profile)
    new_user = UserOut(user_id=new_user)
    return new_user


@app.put("/users/{user_id}", response_model=UserOut)
async def update_user(user_id: int, full_user_profile: FullUserProfile) -> UserOut:
    updated_user = await create_update_user(full_user_profile, user_id)
    updated_user = UserOut(user_id=updated_user)
    return updated_user


@app.delete("/users/{user_id}", response_model=str)
async def remove_user(user_id: int):
    return await delete_user_by_id(user_id)
