from fastapi import APIRouter, HTTPException, status
from fastapi_sqlalchemy import db
from schemas.gallery import ReadGalleryOut
from models.gallery import Gallery


router = APIRouter()


@router.get("/{galleryid}", response_model=ReadGalleryOut)
async def read_gallery(galleryid: int):

    gallery = db.session.query(Gallery).filter_by(gallery_id=galleryid).first()

    if not gallery:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gallery not found")

    result = {
        "owner_id": gallery.owner_id,
        "gallery_name": gallery.gallery_name,
        "gallery_description": gallery.gallery_description,
    }

    return result
