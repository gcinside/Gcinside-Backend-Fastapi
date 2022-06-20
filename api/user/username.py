from fastapi import APIRouter, Depends
from fastapi_sqlalchemy import db
from utils.verify_token import verify_token
from utils.get_subject import get_subject
from schemas.user import Username
from models.account_user import AccountUser


router = APIRouter()


@router.put("/username")
async def username(username: Username, token: str = Depends(verify_token)):
    subject = await get_subject(token)
    db.session.query(AccountUser).filter_by(user_email=subject).update({"user_name": username.username})
    db.session.commit()
    return {"message": "Update username"}
