from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db
from datetime import datetime
import requests
from core.config import settings
from core.const import GOOGLE_TOKEN_ENDPOINT, GOOGLE_USER_INFO
from models.account_user import AccountUser
from utils.generate_token import generate_token


router = APIRouter()


@router.get("/callback")
async def google_callback(error=None, code=None):
    if error:
        raise HTTPException(status_code=400, detail=error)

    params = {
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": settings.GOOGLE_CALLBACK_URL,
        "code": code,
        "grant_type": "authorization_code",
    }

    access_token = requests.post(GOOGLE_TOKEN_ENDPOINT, params=params).json()["access_token"]
    response = requests.get(GOOGLE_USER_INFO, params={"access_token": access_token}).json()

    user = db.session.query(AccountUser).filter_by(user_email=response["email"]).first()

    if user:
        payload = {"sub": user.user_email}
        access_token = generate_token(payload, "access")
        refresh_token = generate_token(payload, "refresh")

        return {"access_token": access_token, "refresh_token": refresh_token}

    else:
        db.session.add(
            AccountUser(
                user_email=response["email"],
                profile_image=response["picture"],
                user_name=response["name"],
                join_date=datetime.utcnow(),
                is_superuser=False,
                is_staff=False,
            )
        )
        db.session.commit()

        payload = {"sub": response["email"]}
        access_token = generate_token(payload, "access")
        refresh_token = generate_token(payload, "refresh")

        return {"access_token": access_token, "refresh_token": refresh_token}
