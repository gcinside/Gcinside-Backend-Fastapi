from fastapi import APIRouter
from . import image

image_router = APIRouter()

image_router.include_router(image.router, prefix="/image")
