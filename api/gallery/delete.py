from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_sqlalchemy import db
from utils.verify_token import verify_token
from utils.get_payload_value import get_payload_value
from schemas.gallery import DeleteGalleryOut
from models.gallery import Gallery
from models.post import Post
from models.user import User


router = APIRouter()


@router.delete("/{galleryid}", response_model=DeleteGalleryOut)
async def delete_gallery(galleryid: int, token: str = Depends(verify_token)):
    email = get_payload_value(token, "sub")
    owner_id, is_staff = db.session.query(User.user_id, User.is_staff).filter_by(user_email=email).first()

    gallery = db.session.query(Gallery).filter_by(gallery_id=galleryid).first()

    if not gallery:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gallery not found")

    if is_staff == False:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are unauthorized to make this request")

    if gallery.owner_id != owner_id and is_staff == False:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are unauthorized to make this request")

    posts = db.session.query(Post).filter_by(gallery_id=galleryid).all()

    if posts:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can't delete gallery that has posts")

    db.session.query(Gallery).filter_by(gallery_id=galleryid).delete()
    db.session.commit()

    return {"message": "Success delete gallery"}
