from fastapi import APIRouter
from .auth.api import auth_router
from .gallery.api import gallery_router
from .post.api import post_router
from .image.api import image_router
from .user.api import user_router
from .report.api import report_router
from .comment.api import comment_router

api_router = APIRouter()

api_router.include_router(auth_router, tags=["auth"])
api_router.include_router(gallery_router, tags=["gallery"])
api_router.include_router(post_router, tags=["post"])
api_router.include_router(image_router, tags=["image"])
api_router.include_router(user_router, tags=["user"])
api_router.include_router(report_router, tags=["report"])
api_router.include_router(comment_router, tags=["comment"])
