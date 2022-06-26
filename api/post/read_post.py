from fastapi import APIRouter, HTTPException, status
from fastapi_sqlalchemy import db
from schemas.post import ReadPostOut
from models.user import User
from models.post import Post


router = APIRouter()


@router.get("/{postid}", response_model=ReadPostOut)
async def read_post(postid: int):

    post = db.session.query(Post).filter_by(post_id=postid).first()
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    user = db.session.query(User).filter_by(user_id=post.author_id).first()

    result = {
        "title": post.post_title,
        "content": post.post_content,
        "image_url": post.post_image,
        "author": user.user_name,
        "created_at": post.created_at,
    }

    return result
