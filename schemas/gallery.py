from pydantic import BaseModel


class CreateGalleryIn(BaseModel):
    gallery_name: str
    gallery_description: str

    class Config:
        schema_extra = {"example": {"gallery_name": "GSM 갤러리", "gallery_description": "GSM 갤러리입니다."}}


class CreateGalleryOut(BaseModel):
    message: str

    class Config:
        schema_extra = {"example": {"message": "Success create gallery"}}


class DeleteGalleryOut(BaseModel):
    message: str

    class Config:
        schema_extra = {"example": {"message": "Success to delete gallery"}}


class ReadGalleryOut(BaseModel):
    owner_id: int
    gallery_name: str
    gallery_description: str

    class Config:
        schema_extra = {
            "example": {
                "owner_id": "1",
                "gallery_name": "GSM 갤러리",
                "gallery_description": "GSM 갤러리입니다.",
            }
        }


class UpdateGalleryIn(BaseModel):
    gallery_name: str
    gallery_description: str

    class Config:
        schema_extra = {"example": {"gallery_name": "GSM 갤러리", "gallery_description": "GSM 갤러리입니다."}}


class UpdateGalleryOut(BaseModel):
    message: str

    class Config:
        schema_extra = {"example": {"message": "Success to update gallery"}}


class ReadGalleryListOut(BaseModel):
    gallery_list: list

    class Config:
        schema_extra = {
            "example": {"gallery_list": [{"id": "1", "owner_id": "1", "name": "GSM 갤러리", "description": "GSM 갤러리입니다."}]}
        }
