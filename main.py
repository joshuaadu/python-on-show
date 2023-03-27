from fastapi import FastAPI
from app.routes.user import create_user_router
from app.exception_handlers import add_exception_handlers
from fake_database.user import users_profile, users_role, users_info


def create_application() -> FastAPI:
    user_router = create_user_router(users_info, users_role, users_profile)

    app = FastAPI()
    app.include_router(user_router)
    add_exception_handlers(app)

    return app


# def create_mock_database():


app = create_application()
