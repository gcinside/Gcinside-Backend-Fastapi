from fastapi import APIRouter
from . import read_user_info, update_profile_image, update_username


user_router = APIRouter()

user_router.include_router(update_profile_image.router, prefix="/user")
user_router.include_router(update_username.router, prefix="/user")
user_router.include_router(read_user_info.router, prefix="/user")
