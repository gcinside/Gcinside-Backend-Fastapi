from fastapi import APIRouter, status, HTTPException
from schemas.auth import Token
from core.config import settings
import jwt


router = APIRouter()


@router.post("/refresh")
async def username(token: Token):
    try:
        a = jwt.decode(token.access_token, settings.JWT_SECRET, algorithms=settings.JWT_ALGORITHM)
        b = jwt.decode(token.refresh_token, settings.JWT_SECRET, algorithms=settings.JWT_ALGORITHM)

        print(a, b)

    except jwt.ExpiredSignatureError:
        pass

    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    else:
        return
