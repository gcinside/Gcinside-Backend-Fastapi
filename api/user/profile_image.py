from fastapi import APIRouter, Depends
from fastapi_sqlalchemy import db
from utils.verify_token import verify_token
from utils.get_payload_value import get_payload_value
from schemas.user import ProfileImageIn, ProfileImageOut
from models.account_user import AccountUser


router = APIRouter()


@router.patch("/image", response_model=ProfileImageOut)
async def profile_image(profile_image: ProfileImageIn, token: str = Depends(verify_token)):
    sub = get_payload_value(token, "sub")
    db.session.query(AccountUser).filter_by(user_email=sub).update({"profile_image": profile_image.profile_image})
    db.session.commit()
    return {"message": "Update image"}
