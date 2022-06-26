from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_sqlalchemy import db
from utils.verify_token import verify_token
from utils.get_payload_value import get_payload_value
from schemas.post import CreatePostIn, CreatePostOut
from models.gallery import Gallery
from models.user import User
from models.post import Post
from datetime import datetime


router = APIRouter()


@router.post("", response_model=CreatePostOut)
async def create_post(upload_post: CreatePostIn, token: str = Depends(verify_token)):

    email = get_payload_value(token, "sub")
    author_id = db.session.query(User).filter_by(user_email=email).first().user_id
    gallery = db.session.query(Gallery).filter_by(gallery_id=upload_post.gallery_id).first()

    if not gallery:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gallery not found")

    db.session.add(
        Post(
            author_id=author_id,
            gallery_id=upload_post.gallery_id,
            post_title=upload_post.title,
            post_content=upload_post.content,
            post_image=upload_post.image_url,
            created_at=datetime.now(),
        )
    )
    db.session.commit()

    return {"message": "Success to upload"}
