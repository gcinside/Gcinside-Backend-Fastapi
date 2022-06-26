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
    image_url: str

    class Config:
        schema_extra = {"example": {"image_url": "https://avatars.githubusercontent.com/u/..."}}


class ProfileImageOut(BaseModel):
    message: str

    class Config:
        schema_extra = {"example": {"message": "Update image"}}


class UserInfoOut(BaseModel):
    id: int
    email: str
    username: str
    profile_image: str

    class Config:
        schema_extra = {
            "example": {
                "id": "1",
                "email": "email",
                "username": "username",
                "profile_image": "https://avatars.githubusercontent.com/u/...",
            }
        }
