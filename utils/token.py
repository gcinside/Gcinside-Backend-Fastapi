from datetime import datetime, timedelta
from core.config import settings
import jwt

def generate_token(payload, token_type):
    if token_type == "access":
        exp = datetime.now() + timedelta(seconds=settings.ACCESS_TOKEN_EXPIRATION_TIME)
    elif token_type == "refresh":
        exp = datetime.now() + timedelta(seconds=settings.REFRESH_TOKEN_EXPIRATION_TIME)
    
    payload["exp"] = exp
    
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)