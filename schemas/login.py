from pydantic import BaseModel


class LoginOut(BaseModel):
    continue_url: str

    class Config:
        schema_extra = {"example": {"continue_url": "https://accounts.google.com/..."}}
