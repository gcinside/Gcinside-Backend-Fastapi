from fastapi import APIRouter
from .google import login, callback

api_router = APIRouter()

api_router.include_router(login.router, prefix="/google", tags=["google_auth"])
api_router.include_router(callback.router, prefix="/google", tags=["google_auth"])
