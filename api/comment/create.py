from fastapi import APIRouter, HTTPException, status, Depends
from fastapi_sqlalchemy import db
from utils.verify_token import verify_token
from utils.get_payload_value import get_payload_value
from models.post import Post
from models.post_comment import PostComment
from models.user import User
from schemas.comment import CreateCommentIn, CreateCommentOut
from datetime import datetime


router = APIRouter()


@router.post("/{postid}/comment", response_model=CreateCommentOut)
async def create_comment(postid: int, upload_comment: CreateCommentIn, token: str = Depends(verify_token)):

    email = get_payload_value(token, "sub")
    user_id = db.session.query(User).filter_by(user_email=email).first().user_id
    post = db.session.query(Post).filter_by(post_id=postid).first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    db.session.add(
        PostComment(
            post_id=postid,
            author_id=user_id,
            comment_content=upload_comment.content,
            is_child_comment=upload_comment.is_child_comment,
            parent_comment_id=upload_comment.parent_comment_id,
            created_at=datetime.now(),
        )
    )
    db.session.commit()

    return {"message": "Success to upload comment"}
