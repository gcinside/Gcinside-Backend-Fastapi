from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db
from datetime import datetime
import requests
from core.config import settings
from core.const import GITHUB_TOKEN_ENDPOINT, GITHUB_USER_INFO, GITHUB_EMAIL_INFO
from models.account_user import AccountUser
from utils.token import generate_token
from urllib.parse import urlparse, parse_qsl

router = APIRouter()


@router.get("/callback")
async def github_callback(error=None, code=None):
    if error:
        raise HTTPException(status_code=400, detail=error)
    
    params = {
        "client_id": settings.GITHUB_CLIENT_ID,
        "client_secret": settings.GITHUB_CLIENT_SECRET,
        "code": code
    }

    access_token = requests.post(GITHUB_TOKEN_ENDPOINT, headers={"Accept": "application/json"}, params=params).json()["access_token"]
    response = requests.get(GITHUB_USER_INFO, headers={"Authorization": "Token " + access_token}).json()
    email = requests.get(GITHUB_EMAIL_INFO, headers={"Authorization": "Token " + access_token}).json()[0]["email"]

    user = db.session.query(AccountUser).filter_by(user_email=email).first()

    if user:
        payload = {"sub": user.user_email}
        access_token = generate_token(payload, "access")
        refresh_token = generate_token(payload, "refresh")

        return {"access_token": access_token, "refresh_token": refresh_token}

    else:
        db.session.add(
            AccountUser(
                user_email=email,
                profile_image=response["avatar_url"],
                user_name=response["login"],
                join_date=datetime.utcnow(),
                is_superuser=False,
                is_staff=False,
            )
        )
        db.session.commit()

        payload = {"sub": email}
        access_token = generate_token(payload, "access")
        refresh_token = generate_token(payload, "refresh")

        return {"access_token": access_token, "refresh_token": refresh_token}
