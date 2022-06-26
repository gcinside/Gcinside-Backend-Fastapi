from fastapi import APIRouter
from fastapi_sqlalchemy import db
from schemas.gallery import ReadGalleryListOut
from models.gallery import Gallery


router = APIRouter()


@router.get("", response_model=ReadGalleryListOut)
async def read_gallery_list():

    result = []

    for gallery in db.session.query(Gallery).all():
        result.append(
            {
                "id": gallery.gallery_id,
                "owner_id": gallery.owner_id,
                "name": gallery.gallery_name,
                "description": gallery.gallery_description,
            }
        )

    return {"gallery_list": result}
