from fastapi import APIRouter, HTTPException, status
from fastapi_sqlalchemy import db
from schemas.user import UserInfoOut
from models.user import User


router = APIRouter()


@router.get("/{userid}", response_model=UserInfoOut)
async def read_user_info(userid: int):
    user = db.session.query(User).filter_by(user_id=userid).first()

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return {
        "id": user.user_id,
        "email": user.user_email,
        "username": user.user_name,
        "profile_image": user.user_profile_image,
    }
