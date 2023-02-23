from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Union, Optional
app = FastAPI()


class Role(BaseModel):
    name: str = Field(
        title="Role name",
        description="Current role of the user",
        max_length=14, min_length=5
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
    company_name: str = Field(alias="company")


def get_user_info() -> User:
    user_role = {
        "name": "developer lead",
        "id": 1,
        "description": "PaySwitch developer lead"
    }
    user_role = Role(**user_role)
    user_profile = {
        "title": "Software Developer",
        "description": "PaySwitch software developer",
        "address": "accra",
        "roles": [user_role]
    }
    user_profile = Profile(**user_profile)
    print(user_profile)

    user_info = {
        "name": "Joe Men",
        "age": 20
        # "profile": user_profile
    }
    user_info = User(**user_info)
    print(user_info)
    full_user_profile = {
        **user_info.dict(),
        **user_profile.dict(),
        "company": "PaySwitch"
    }

    full_user_profile = FullUserProfile(**full_user_profile)
    print(full_user_profile)
    return full_user_profile


@app.get("/", response_class=PlainTextResponse)
def home():
    return "Hello World from Ghana"


@app.get("/about", response_class=JSONResponse)
def about():
    return {"name": "John Doe", "address": "East Legon"}


@app.get("/user/me", response_model=FullUserProfile)
def getuser():
    user_info = get_user_info()
    return user_info


# practice using decorators
def add_age(fn):
    def wrapper():
        age = 10
        return fn(age)
    return wrapper


@app.get("/user/age")
@add_age
def user(age):
    return "name: Jo, age:{}".format(age)
