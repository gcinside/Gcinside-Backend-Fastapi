from fastapi import HTTPException, status
from core.config import settings
import jwt


def get_payload_value(token: str, key: str):
    try:
        value = jwt.decode(token, settings.JWT_SECRET, algorithms=settings.JWT_ALGORITHM)[key]

    except KeyError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    return value
