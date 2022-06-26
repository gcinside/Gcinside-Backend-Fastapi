from fastapi import APIRouter, status, HTTPException
from schemas.auth import RefreshIn, RefreshOut
from utils.generate_token import generate_token
from utils.get_payload_value import get_payload_value
import jwt


router = APIRouter()


@router.post("/refresh", response_model=RefreshOut)
async def refresh(token: RefreshIn):
    try:
        token_type = get_payload_value(token.refresh_token, "type")
        if token_type != "refresh_token":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

        sub = get_payload_value(token.refresh_token, "sub")

        token = generate_token({"sub": sub}, "access")
        return {"access_token": token}

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")

    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
