from fastapi import APIRouter, Depends
from fastapi_sqlalchemy import db
from utils.verify_token import verify_token
from utils.get_payload_value import get_payload_value
from schemas.user import UsernameIn, UsernameOut
from models.account_user import AccountUser


router = APIRouter()


@router.patch("/username", response_model=UsernameOut)
async def username(username: UsernameIn, token: str = Depends(verify_token)):
    sub = get_payload_value(token, "sub")
    db.session.query(AccountUser).filter_by(user_email=sub).update({"user_name": username.username})
    db.session.commit()
    return {"message": "Update username"}
