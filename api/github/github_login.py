from fastapi import APIRouter
from urllib.parse import urlencode
from core.config import settings
from core.const import GITHUB_AUTH_ENDPOINT

router = APIRouter()


@router.get("/login")
async def github_login():
    params = {
        "client_id": settings.GITHUB_CLIENT_ID,
        "redirect_uri": settings.GITHUB_CALLBACK_URL,
        "scope": settings.GITHUB_AUTH_SCOPE,
    }

    return {"continue": GITHUB_AUTH_ENDPOINT + "?" + urlencode(params)}
