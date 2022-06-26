from fastapi import APIRouter, HTTPException, status
from fastapi_sqlalchemy import db
from schemas.post import ReadPostListOut
from models.post import Post

router = APIRouter()


@router.get("", response_model=ReadPostListOut)
async def read_post_list(galleryid: int, page: int = 1):

    if page < 1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Page must be greater than 0")

    result = []

    for post in (
        db.session.query(Post)
        .filter_by(gallery_id=galleryid)
        .order_by(Post.post_id.desc)
        .limit(30)
        .offset((page - 1) * 30)
        .all()
    ):
        result.append(
            {
                "post_id": post.post_id,
                "author_id": post.author_id,
                "gallery_id": post.gallery_id,
                "post_title": post.post_title,
                "post_content": post.post_content,
                "post_image": post.post_image,
                "created_at": post.created_at,
            }
        )

    return {"post_list": result}
