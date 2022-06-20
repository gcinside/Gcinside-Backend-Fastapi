from fastapi import APIRouter, status, HTTPException
from schemas.auth import Token
from core.config import settings
from utils.generate_token import generate_token
import jwt


router = APIRouter()


@router.post("/refresh")
async def username(token: Token):
    try:
        sub = jwt.decode(token.refresh_token, settings.JWT_SECRET, algorithms=settings.JWT_ALGORITHM)["sub"]
        token = generate_token({"sub": sub}, "access")
        return {"access_token": token}

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")

    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
