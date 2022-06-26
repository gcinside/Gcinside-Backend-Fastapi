from fastapi import APIRouter
from . import create, read_gallery, read_list, update, delete

gallery_router = APIRouter()

gallery_router.include_router(create.router, prefix="/gallery")
gallery_router.include_router(delete.router, prefix="/gallery")
gallery_router.include_router(read_gallery.router, prefix="/gallery")
gallery_router.include_router(update.router, prefix="/gallery")
gallery_router.include_router(read_list.router, prefix="/gallery")
