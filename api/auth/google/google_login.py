from fastapi import APIRouter
from urllib.parse import urlencode
from core.config import settings
from core.const import GOOGLE_AUTH_ENDPOINT
from schemas.login import LoginOut

router = APIRouter()


@router.get("/login", response_model=LoginOut)
async def google_login():
    params = {
        "client_id": settings.GOOGLE_CLIENT_ID,
        "redirect_uri": settings.GOOGLE_CALLBACK_URL,
        "scope": settings.GOOGLE_AUTH_SCOPE,
        "access_type": "offline",
        "response_type": "code",
    }

    return {"continue_url": GOOGLE_AUTH_ENDPOINT + "?" + urlencode(params)}
