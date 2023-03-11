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


def get_user_info(user_id: int = 0) -> FullUserProfile:
    print(users_role[0])
    user_role = Role(**users_role[user_id])
    users_profile[user_id]["roles"].append(user_role)
    user_profile = Profile(**users_profile[user_id])
    user_info = User(**users_info[user_id])
    full_user_profile = {
        **user_info.dict(),
        **user_profile.dict(),
        "department": "Tech"
    }

    full_user_profile = FullUserProfile(**full_user_profile)
    print(full_user_profile)
    return full_user_profile


def create_user(full_user_profile: FullUserProfile):
    new_user_id = len(users_info)
    users_info[new_user_id] = {
        "name": full_user_profile.name,
        "age": full_user_profile.age
    }
    users_profile[new_user_id] = {
        "title": full_user_profile.title,
        "description": full_user_profile.description,
        "address": full_user_profile.address,
        "roles": full_user_profile.roles
    }
    print(users_role, "\n\n", users_info, "\n\n", users_profile)
    return new_user_id


def get_users_with_pagination(start: int, limit: int) -> list[FullUserProfile]:
    keys = list(users_info.keys())
    print(keys)
    keys_length = len(keys)
    users = []
    for index in range(0, keys_length):
        if index < start:
            continue
        if len(users) >= limit:
            break
        print("current key is {}".format(keys[index]))
        users.append(get_user_info(keys[index]))
    return users


@app.get("/", response_class=PlainTextResponse)
def home():
    return "Hello World from Ghana"


@app.get("/about", response_class=JSONResponse)
def about():
    return {"name": "John Doe", "address": "East Legon"}


@app.get("/user/me", response_model=FullUserProfile)
def getuser():
    full_user_profile = get_user_info()
    return full_user_profile


@app.get("/users/{user_id}", response_model=FullUserProfile)
def get_user_by_id(user_id: int):
    full_user_profile = get_user_info(user_id)
    return full_user_profile


@app.get("/users", response_model=MultipleUsersProfile)
def get_all_users(start: int = 0, limit: int = 2):
    users = get_users_with_pagination(start, limit)
    users_list = MultipleUsersProfile(users=users)
    return users_list


@app.post("/users", response_model=UserOut)
def add_user(full_user_profile: FullUserProfile) -> UserOut:
    print(full_user_profile)
    new_user = create_user(full_user_profile)
    new_user = UserOut(user_id=new_user)
    return new_user
