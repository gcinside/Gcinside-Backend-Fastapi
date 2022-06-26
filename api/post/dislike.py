from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_sqlalchemy import db
from utils.verify_token import verify_token
from utils.get_payload_value import get_payload_value
from schemas.post import DislikePostOut
from models.post import Post
from models.user import User
from models.post_like import PostLike


router = APIRouter()


@router.post("/{postid}/dislike", response_model=DislikePostOut)
async def dislike_post(postid: int, token: str = Depends(verify_token)):
    """
    이미 싫어요 눌렀을때 요청 시 싫어요 취소
    """

    email = get_payload_value(token, "sub")
    user_id = db.session.query(User).filter_by(user_email=email).first().user_id
    post = db.session.query(Post).filter_by(post_id=postid).first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    dislike = db.session.query(PostLike).filter_by(post_id=postid, user_id=user_id, like_type=0).first()

    if dislike == None:
        db.session.add(PostLike(post_id=postid, user_id=user_id, like_type=0))
        db.session.commit()
        return {"message": "Success to dislike post"}

    elif dislike != None:
        db.session.query(PostLike).filter_by(post_id=postid, user_id=user_id).delete()
        db.session.commit()
        return {"message": "Success to canceling dislike"}
