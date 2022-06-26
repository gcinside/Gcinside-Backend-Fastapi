from fastapi import APIRouter, Depends, UploadFile, File
from fastapi_sqlalchemy import db
from utils.verify_token import verify_token
from schemas.post import UploadImageOut
from core.config import settings
from models.image import Image
import boto3

router = APIRouter()


@router.post("", response_model=UploadImageOut)
async def upload_image(image: UploadFile = File(...), token: str = Depends(verify_token)):
    try:
        image_id = db.session.query(Image.image_id).order_by(Image.image_id.desc()).first()[0]
    except:
        image_id = 1

    s3 = boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY,
        aws_secret_access_key=settings.AWS_SECRET_KEY,
    )
    s3.upload_fileobj(image.file, settings.S3_BUCKET_NAME, f"{str(image_id)}.png")
    image_url = f"https://gcinside.s3.ap-northeast-2.amazonaws.com/{str(image_id)}.png"

    db.session.add(Image(image_url=image_url))
    db.session.commit()

    return {"message": "success", "image_url": image_url}
