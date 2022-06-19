from fastapi import APIRouter
from urllib.parse import urlencode
from core.config import settings
from core.const import GOOGLE_AUTH_ENDPOINT

router = APIRouter()


@router.get("/login")
async def google_login():
    params = {
        "client_id": settings.GOOGLE_CLIENT_ID,
        "redirect_uri": settings.GOOGLE_CALLBACK_URL,
        "scope": settings.GOOGLE_AUTH_SCOPE,
        "access_type": "offline",
        "response_type": "code",
    }

    return {"continue": GOOGLE_AUTH_ENDPOINT + "?" + urlencode(params)}
