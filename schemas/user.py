from pydantic import BaseModel


class UsernameIn(BaseModel):
    username: str

    class Config:
        schema_extra = {"example": {"username": "Nickname"}}


class UsernameOut(BaseModel):
    message: str

    class Config:
        schema_extra = {"example": {"message": "Update username"}}


class ProfileImageIn(BaseModel):
    profile_image: str

    class Config:
        schema_extra = {"example": {"profile_image": "https://avatars0.githubusercontent.com/u/..."}}


class ProfileImageOut(BaseModel):
    message: str

    class Config:
        schema_extra = {"example": {"message": "Update image"}}
