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
    id: str
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


users_info = {
    "admin": {
        "name": "Joe Men",
        "age": 20
    },
    "user_1": {
        "name": "Roe Ken",
        "age": 20
    },
    "user_2": {
        "name": "Betty Lov",
        "age": 20
    },
}

users_role = {
    "admin": {
        "name": "developer lead",
        "id": 1,
        "description": "PaySwitch developer lead"
    },
    "user_1": {
        "name": "UI developer",
        "id": 1,
        "description": "PaySwitch UI developer"
    },
    "user_2": {
        "name": "Mobile developer",
        "id": 1,
        "description": "PaySwitch Mobile developer"
    }

}

users_profile = {
    "admin": {
        "title": "Software Developer",
        "description": "PaySwitch software developer",
        "address": "accra",
        "roles": []
    },
    "user_1": {
        "title": "Software Developer",
        "description": "PaySwitch software developer",
        "address": "Koforidua",
        "roles": []
    },
    "user_2": {
        "title": "Software Developer",
        "description": "PaySwitch software developer",
        "address": "Tema",
        "roles": []
    },
}


def get_user_info(user_id: str = "admin") -> User:
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
    pass


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


@app.get("/user/{user_id}", response_model=FullUserProfile)
def get_user_by_id(user_id: str):
    full_user_profile = get_user_info(user_id)
    return full_user_profile


@app.post("/users")
def add_user(full_user_profile: FullUserProfile):
    print(full_user_profile)
    pass







# practice using decorators
# def add_age(fn):
#     def wrapper():
#         age = 10
#         return fn(age)
#     return wrapper

# @app.get("/user/age")
# @add_age
# def user(age):
#     return "name: Jo, age:{}".format(age)
