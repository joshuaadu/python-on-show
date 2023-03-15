from fastapi import APIRouter
from fastapi.responses import (
    PlainTextResponse,
    JSONResponse
)
from app.services.user import UserService
from app.schemas.user import (UserOut, MultipleUsersProfile, FullUserProfile)


def create_user_router() -> APIRouter:
    user_router = APIRouter()
    user_service = UserService()

    @user_router.get("/", response_class=PlainTextResponse)
    async def home():
        return "Hello World from Ghana"

    @user_router.get("/about", response_class=JSONResponse)
    async def about():
        return {"name": "John Doe", "address": "East Legon"}

    @user_router.get("/user/me", response_model=FullUserProfile)
    async def getuser():
        full_user_profile = await user_service.get_user_info()
        return full_user_profile

    @user_router.get("/users/{user_id}", response_model=FullUserProfile)
    async def get_user_by_id(user_id: int):
        """
        Endpoint for retrieving a FullUserProfile by the user's unique integer id
        :param user_id:
        :return:
        """
        full_user_profile = await user_service.get_user_info(user_id)
        return full_user_profile

    @user_router.get("/users", response_model=MultipleUsersProfile)
    async def get_all_users_pagination(start: int = 0, limit: int = 2):
        users, total = await user_service.get_users_with_pagination(start, limit)
        users_list = MultipleUsersProfile(users=users, total=total)
        return users_list

    @user_router.post("/users", response_model=UserOut)
    async def add_user(full_user_profile: FullUserProfile) -> UserOut:
        new_user = await user_service.create_update_user(full_user_profile)
        new_user = UserOut(user_id=new_user)
        return new_user

    @user_router.put("/users/{user_id}", response_model=UserOut)
    async def update_user(user_id: int, full_user_profile: FullUserProfile) -> UserOut:
        updated_user = await user_service.create_update_user(full_user_profile, user_id)
        updated_user = UserOut(user_id=updated_user)
        return updated_user

    @user_router.delete("/users/{user_id}", response_model=str)
    async def remove_user(user_id: int):
        return await user_service.delete_user_by_id(user_id)

    return user_router
