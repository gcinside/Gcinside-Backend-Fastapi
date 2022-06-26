from fastapi import APIRouter
from . import create, read, delete, update

comment_router = APIRouter()
comment_router.include_router(read.router, prefix="/post")
comment_router.include_router(delete.router, prefix="/post")
comment_router.include_router(create.router, prefix="/post")
comment_router.include_router(update.router, prefix="/post")
