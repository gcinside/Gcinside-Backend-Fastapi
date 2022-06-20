from fastapi import APIRouter
from .google import google_login, google_callback
from .github import github_login, github_callback
from .auth import refresh
from .user import username, profile_image


api_router = APIRouter()

api_router.include_router(google_login.router, prefix="/google", tags=["google_auth"])
api_router.include_router(google_callback.router, prefix="/google", tags=["google_auth"])

api_router.include_router(github_login.router, prefix="/github", tags=["github_auth"])
api_router.include_router(github_callback.router, prefix="/github", tags=["github_auth"])

api_router.include_router(username.router, prefix="/user", tags=["user"])
api_router.include_router(profile_image.router, prefix="/user", tags=["user"])

api_router.include_router(refresh.router, prefix="/auth", tags=["auth"])
