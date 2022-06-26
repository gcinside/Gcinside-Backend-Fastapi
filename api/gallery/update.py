from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_sqlalchemy import db
from utils.verify_token import verify_token
from utils.get_payload_value import get_payload_value
from schemas.gallery import UpdateGalleryIn, UpdateGalleryOut
from models.gallery import Gallery
from models.user import User


router = APIRouter()


@router.put("/{galleryid}", response_model=UpdateGalleryOut)
async def update_gallery(galleryid: int, update_gallery: UpdateGalleryIn, token: str = Depends(verify_token)):

    email = get_payload_value(token, "sub")
    user_id = db.session.query(User).filter_by(user_email=email).first().user_id
    gallery = db.session.query(Gallery).filter_by(gallery_id=galleryid).first()

    if not gallery:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gallery not found")

    if user_id != gallery.owner_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are unauthorized to make this request")

    db.session.query(Gallery).filter_by(gallery_id=galleryid).update(
        {
            "gallery_name": update_gallery.gallery_name,
            "gallery_description": update_gallery.gallery_description,
        }
    )
    db.session.commit()

    return {"message": "Success update gallery"}
