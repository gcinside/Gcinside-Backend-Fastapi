from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_sqlalchemy import db
from utils.verify_token import verify_token
from utils.get_payload_value import get_payload_value
from schemas.post import DeletePostOut
from models.post import Post
from models.user import User
from models.post_comment import PostComment
from models.post_like import PostLike


router = APIRouter()


@router.delete("/{postid}", response_model=DeletePostOut)
async def delete_post(postid: int, token: str = Depends(verify_token)):

    email = get_payload_value(token, "sub")
    user_id, is_staff = db.session.query(User.user_id, User.is_staff).filter_by(user_email=email).first()
    post = db.session.query(Post).filter_by(post_id=postid).first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    if user_id != post.author_id and is_staff == False:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are unauthorized to make this request")

    db.session.query(PostComment).filter_by(post_id=postid).delete()
    db.session.query(PostLike).filter_by(post_id=postid).delete()
    db.session.query(Post).filter_by(post_id=postid).delete()
    db.session.commit()

    return {"message": "Success to delete"}
