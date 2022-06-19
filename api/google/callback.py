from fastapi import APIRouter, HTTPException
import requests
from core.config import settings
from core.const import GOOGLE_TOKEN_ENDPOINT, GOOGLE_USER_INFO

router = APIRouter()


@router.get("/callback")
async def google_callback(error = None, code = None):
    if error:
        raise HTTPException(status_code = 400, detail = error)
    
    params = {
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": settings.GOOGLE_CALLBACK_URI,
        "code": code,
        "grant_type": "authorization_code",
    }

    access_token = requests.post(GOOGLE_TOKEN_ENDPOINT, params=params).json()["access_token"]
    response = requests.get(GOOGLE_USER_INFO, params={"access_token": access_token}).json()
    # name, email, picture