from fastapi import APIRouter, HTTPException, status
from fastapi_sqlalchemy import db
from schemas.post import ReadPopularPostListOut
from models.post import Post

router = APIRouter()


@router.get("/popular")
async def read_popular_post_list(galleryid: int):

    result = []

    for post in db.session.query(Post).filter_by(gallery_id=galleryid).order_by(Post.like.desc()).limit(20).all():
        result.append(
            {
                "post_id": post.post_id,
                "author_id": post.author_id,
                "gallery_id": post.gallery_id,
                "post_title": post.post_title,
                "post_content": post.post_content,
                "post_image": post.post_image,
                "created_at": post.created_at,
                "like": post.like,
                "dislike": post.dislike,
            }
        )

    return {"popular_post_list": result}
