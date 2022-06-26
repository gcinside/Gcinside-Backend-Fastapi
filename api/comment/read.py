from fastapi import APIRouter, HTTPException, status
from fastapi_sqlalchemy import db
from models.post import Post
from models.post_comment import PostComment
from schemas.comment import ReadCommentOut

router = APIRouter()


@router.get("/{postid}/comment", response_model=ReadCommentOut)
async def read_comment_list(postid: int):

    post = db.session.query(Post).filter_by(post_id=postid).first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    result = []

    for comment in db.session.query(PostComment).filter_by(post_id=postid).all():
        result.append(
            {
                "id": comment.comment_id,
                "author_id": comment.author_id,
                "comment_content": comment.comment_content,
                "created_at": comment.created_at,
            }
        )
        if comment.is_child_comment == True:
            result[-1]["is_child_comment"] = True
            result[-1]["parent_comment_id"] = comment.parent_comment_id
        else:
            result[-1]["is_child_comment"] = False
            result[-1]["parent_comment_id"] = None

    return {"comment_list": result}
