from fastapi import (
    APIRouter,
    Depends
)
from app.services.user import UserService
from app.schemas.user import (UserOut, MultipleUsersProfile, FullUserProfile)
from app.dependencies import rate_limit


def create_user_router(users_info: dict, users_role: dict, users_profile: dict) -> APIRouter:
    # print(users_info, users_role, users_profile)
    user_router = APIRouter(
        prefix="/users",
        tags=["Users"],
        dependencies=[Depends(rate_limit)]
    )
    user_service = UserService(users_info, users_role, users_profile)

    @user_router.get("/me", response_model=FullUserProfile)
    async def getuser():
        full_user_profile = await user_service.get_user_info()
        return full_user_profile

    @user_router.get("/", response_model=MultipleUsersProfile)
    async def get_all_users_pagination(start: int = 0, limit: int = 2):
        users, total = await user_service.get_users_with_pagination(start, limit)
        users_list = MultipleUsersProfile(users=users, total=total)
        return users_list

    @user_router.post("/", response_model=UserOut, status_code=201)
    async def add_user(full_user_profile: FullUserProfile) -> UserOut:
        print(full_user_profile.json())
        new_user = await user_service.create_update_user(full_user_profile)
        new_user = UserOut(user_id=new_user)
        return new_user

    @user_router.get("/{user_id}", response_model=FullUserProfile)
    async def get_user_by_id(user_id: int):
        """
        Endpoint for retrieving a FullUserProfile by the user's unique integer id
        :param user_id:
        :return:
        """
        # try:
        full_user_profile = await user_service.get_user_info(user_id)
        # except KeyError:
        #     raise HTTPException(status_code=404, detail={"msg": "User not found", "user_id": user_id})
        return full_user_profile

    @user_router.put("/{user_id}", response_model=UserOut)
    async def update_user(user_id: int, full_user_profile: FullUserProfile) -> UserOut:
        updated_user = await user_service.create_update_user(full_user_profile, user_id)
        updated_user = UserOut(user_id=updated_user)
        return updated_user

    @user_router.delete("/{user_id}", response_model=str)
    async def remove_user(user_id: int):
        # try:
        response = await user_service.delete_user_by_id(user_id)
        # except KeyError:
        #     raise HTTPException(status_code=404, detail={"msg": "User doesn't exist", "user_id": user_id})
        return response
    return user_router
