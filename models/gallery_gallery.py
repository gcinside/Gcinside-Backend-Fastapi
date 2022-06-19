from sqlalchemy import Column, ForeignKey, String, Integer, Text
from sqlalchemy.orm import relationship
from db.base import Base

class GalleryGallery(Base):
    __tablename__ = 'gallery_gallery'

    gallery_id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(ForeignKey('account_user.user_id'), nullable=False, index=True)
    gallery_name = Column(String(20), nullable=False)
    gallery_description = Column(Text, nullable=False)

    owner = relationship('AccountUser')