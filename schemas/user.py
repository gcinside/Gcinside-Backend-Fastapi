from pydantic import BaseModel


class Username(BaseModel):
    username: str


class ProfileImage(BaseModel):
    profile_image: str
