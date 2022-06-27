from fastapi import APIRouter

from . import create, dislike, like, read_list, read_post, update, delete, read_popular_list


post_router = APIRouter()

post_router.include_router(create.router, prefix="/post")
post_router.include_router(read_post.router, prefix="/post")
post_router.include_router(update.router, prefix="/post")
post_router.include_router(delete.router, prefix="/post")
post_router.include_router(like.router, prefix="/post")
post_router.include_router(dislike.router, prefix="/post")
post_router.include_router(read_list.router, prefix="/post")
post_router.include_router(read_popular_list.router, prefix="/post")
