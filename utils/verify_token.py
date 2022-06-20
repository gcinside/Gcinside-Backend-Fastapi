from fastapi import Header, status, HTTPException
from core.config import settings
import jwt


async def verify_token(Authorization=Header()):
    token = Authorization.split(" ")[1]
    try:
        jwt.decode(token, settings.JWT_SECRET, algorithms=settings.JWT_ALGORITHM)

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")

    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    return token
