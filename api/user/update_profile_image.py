from fastapi import APIRouter, Depends
from fastapi_sqlalchemy import db
from utils.verify_token import verify_token
from utils.get_payload_value import get_payload_value
from schemas.user import ProfileImageIn, ProfileImageOut
from models.user import User


router = APIRouter()


@router.patch("/image", response_model=ProfileImageOut)
async def update_profile_image(profile_image: ProfileImageIn, token: str = Depends(verify_token)):
    email = get_payload_value(token, "sub")
    db.session.query(User).filter_by(user_email=email).update({"profile_image": profile_image.image_url})
    db.session.commit()
    return {"message": "Update image"}
