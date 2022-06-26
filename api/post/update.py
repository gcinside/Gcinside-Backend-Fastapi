from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_sqlalchemy import db
from utils.verify_token import verify_token
from utils.get_payload_value import get_payload_value
from schemas.post import UpdatePostIn, UpdatePostOut
from models.post import Post
from models.user import User


router = APIRouter()


@router.put("/{postid}", response_model=UpdatePostOut)
async def upload_post(postid: int, update_post: UpdatePostIn, token: str = Depends(verify_token)):

    email = get_payload_value(token, "sub")
    user_id = db.session.query(User).filter_by(user_email=email).first().user_id
    post = db.session.query(Post).filter_by(post_id=postid).first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    if user_id != post.author_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User is not author")

    db.session.query(Post).filter_by(post_id=postid).update(
        {
            Post.post_title: update_post.title,
            Post.post_content: update_post.content,
            Post.post_image: update_post.image_url,
        }
    )
    db.session.commit()

    return {"message": "Success to update"}
