from fastapi import APIRouter
from . import create, view

report_router = APIRouter()


report_router.include_router(create.router, prefix="/report")
report_router.include_router(view.router, prefix="/report")
