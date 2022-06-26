from db.base import Base
from sqlalchemy import Column, Text, Integer


class Image(Base):
    __tablename__ = "image"

    image_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    image_url = Column(Text, nullable=False)
