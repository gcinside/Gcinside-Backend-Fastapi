from urllib.request import Request
from fastapi import APIRouter
from schemas.username import Username


router = APIRouter()


@router.put("/username")
async def username(req: Username):
    pass
