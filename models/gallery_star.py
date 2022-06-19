from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from db.base import Base


class GalleryStar(Base):
    __tablename__ = "gallery_star"

    star_id = Column(Integer, primary_key=True, index=True)
    gallery_id = Column(ForeignKey("gallery_gallery.gallery_id"), nullable=False, index=True)
    user_id = Column(ForeignKey("account_user.user_id"), nullable=False, index=True)

    gallery = relationship("GalleryGallery")
    user = relationship("AccountUser")
