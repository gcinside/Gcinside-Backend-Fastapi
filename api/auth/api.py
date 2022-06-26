from fastapi import APIRouter
from .google import google_login, google_callback
from .github import github_login, github_callback
from . import refresh


auth_router = APIRouter()

auth_router.include_router(google_login.router, prefix="/auth/google")
auth_router.include_router(google_callback.router, prefix="/auth/google")

auth_router.include_router(github_login.router, prefix="/auth/github")
auth_router.include_router(github_callback.router, prefix="/auth/github")

auth_router.include_router(refresh.router, prefix="/auth")
