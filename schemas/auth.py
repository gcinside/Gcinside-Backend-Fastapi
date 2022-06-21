from pydantic import BaseModel


class RefreshIn(BaseModel):
    refresh_token: str

    class Config:
        schema_extra = {"example": {"refresh_token": "eyJhb..."}}


class RefreshOut(BaseModel):
    access_token: str

    class Config:
        schema_extra = {"example": {"access_token": "eyJhb..."}}
