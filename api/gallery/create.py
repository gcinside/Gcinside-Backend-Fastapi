from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_sqlalchemy import db
from utils.verify_token import verify_token
from utils.get_payload_value import get_payload_value
from schemas.gallery import CreateGalleryIn, CreateGalleryOut
from models.gallery import Gallery
from models.user import User


router = APIRouter()


@router.post("", response_model=CreateGalleryOut)
async def create_gallery(create_gallery: CreateGalleryIn, token: str = Depends(verify_token)):
    email = get_payload_value(token, "sub")
    owner_id, is_staff = db.session.query(User.user_id, User.is_staff).filter_by(user_email=email).first()
    if is_staff == False:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are unauthorized to make this request",
        )

    gallery = db.session.query(Gallery).filter_by(gallery_name=create_gallery.gallery_name).first()
    if gallery:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Gallery already exists")

    db.session.add(
        Gallery(
            owner_id=owner_id,
            gallery_name=create_gallery.gallery_name,
            gallery_description=create_gallery.gallery_description,
        )
    )
    db.session.commit()

    return {"message": "Success create gallery"}
