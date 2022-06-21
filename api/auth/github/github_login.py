from fastapi import APIRouter
from urllib.parse import urlencode
from core.config import settings
from core.const import GITHUB_AUTH_ENDPOINT
from schemas.login import LoginOut

router = APIRouter()


@router.get("/login", response_model=LoginOut)
async def github_login():
    params = {
        "client_id": settings.GITHUB_CLIENT_ID,
        "redirect_uri": settings.GITHUB_CALLBACK_URL,
        "scope": settings.GITHUB_AUTH_SCOPE,
    }

    return {"continue_url": GITHUB_AUTH_ENDPOINT + "?" + urlencode(params)}
