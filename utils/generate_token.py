from core.config import settings
from datetime import datetime, timedelta, timezone
import jwt


def generate_token(payload, token_type):
    if token_type == "access":
        exp = datetime.now(timezone(timedelta(hours=9))) + timedelta(seconds=settings.ACCESS_TOKEN_EXPIRATION_TIME)
    elif token_type == "refresh":
        exp = datetime.now(timezone(timedelta(hours=9))) + timedelta(seconds=settings.REFRESH_TOKEN_EXPIRATION_TIME)

    payload["type"] = f"{token_type}_token"
    payload["exp"] = exp
    payload["iat"] = datetime.now(timezone(timedelta(hours=9)))

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
