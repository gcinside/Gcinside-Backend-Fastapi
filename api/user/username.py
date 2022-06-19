from fastapi import APIRouter
from core.config import settings
from schemas.user import Username


router = APIRouter()


@router.put("/username")
async def username(username: Username):
    pass
