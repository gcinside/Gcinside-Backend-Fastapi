from fastapi import APIRouter, Depends
from fastapi_sqlalchemy import db
from utils.verify_token import verify_token
from utils.get_subject import get_subject
from schemas.user import ProfileImage
from models.account_user import AccountUser


router = APIRouter()


@router.put("/image")
async def profile_image(profile_image: ProfileImage, token: str = Depends(verify_token)):
    subject = await get_subject(token)
    db.session.query(AccountUser).filter_by(user_email=subject).update({"profile_image": profile_image.profile_image})
    db.session.commit()
    return {"message": "Update image"}
