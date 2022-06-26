from db.base import Base
from sqlalchemy import Column, ForeignKey, String, Text, Integer
from sqlalchemy.orm import relationship


class Gallery(Base):
    __tablename__ = "gallery"

    gallery_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    owner_id = Column(ForeignKey("user.user_id"), nullable=False, index=True)
    gallery_name = Column(String(100), nullable=False, index=True)
    gallery_description = Column(Text, nullable=False)

    owner = relationship("User")
