from fastapi import FastAPI, Request
from fastapi_sqlalchemy import DBSessionMiddleware
from api.api import api_router
from core.config import settings


app = FastAPI(title=settings.PROJECT_NAME)
app.add_middleware(DBSessionMiddleware, db_url=settings.DB_URL)
app.include_router(api_router)


if __name__ == "__main__":
    import os

    os.system("uvicorn main:app --host 0.0.0.0 --port 80 --reload")
