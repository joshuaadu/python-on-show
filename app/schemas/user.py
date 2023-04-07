from pydantic import BaseModel, Field
from typing import Optional


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
    department: str
    # department_name: str = Field(alias="department")
    # I had the following error during testing:
    # {'detail': [{'loc': ['body', 'department'], 'msg': 'field required', 'type': 'value_error.missing'}]}


class MultipleUsersProfile(BaseModel):
    users: list[FullUserProfile]
    total: int


class UserOut(BaseModel):
    user_id: int = Field(title="User ID", description="Id of newly created user")

