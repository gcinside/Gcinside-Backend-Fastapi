from fastapi import APIRouter, HTTPException, status
from fastapi_sqlalchemy import db
from schemas.post import ReadPostOut
from models.user import User
from models.post import Post


router = APIRouter()


@router.get("/{postid}", response_model=ReadPostOut)
async def read_post(postid: int):

    post = db.session.query(Post).filter_by(post_id=postid).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    result = {
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

    return {"post": result}
