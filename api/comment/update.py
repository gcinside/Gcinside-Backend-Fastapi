from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_sqlalchemy import db
from utils.verify_token import verify_token
from utils.get_payload_value import get_payload_value
from models.post import Post
from models.post_comment import PostComment
from models.user import User
from schemas.comment import UpdateCommentIn, UpdateCommentOut

router = APIRouter()


@router.put("/{postid}/comment/{commentid}", response_model=UpdateCommentOut)
async def update_post(postid: int, commentid: int, update_comment: UpdateCommentIn, token: str = Depends(verify_token)):

    email = get_payload_value(token, "sub")
    user_id = db.session.query(User).filter_by(user_email=email).first().user_id
    post = db.session.query(Post).filter_by(post_id=postid).first()
    comment = db.session.query(PostComment).filter_by(comment_id=commentid).first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    if comment == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

    if user_id != comment.author_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not the author of this comment")

    db.session.query(PostComment).filter_by(comment_id=commentid).update({"comment_content": update_comment.content})
    db.session.commit()

    return {"message": "Success to update comment"}
