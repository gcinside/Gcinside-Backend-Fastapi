from fastapi import APIRouter, Depends
from utils.verify_token import verify_token
from schemas.user import Username


router = APIRouter()


@router.put("/username", dependencies=[Depends(verify_token)])
async def username(username: Username):
    pass
