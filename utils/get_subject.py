from core.config import settings
import jwt


async def get_subject(token: str):
    sub = jwt.decode(token, settings.JWT_SECRET, algorithms=settings.JWT_ALGORITHM)["sub"]
    return sub
