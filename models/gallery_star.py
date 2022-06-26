from db.base import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class GalleryStar(Base):
    __tablename__ = "gallery_star"

    star_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    gallery_id = Column(ForeignKey("gallery.gallery_id"), nullable=False, index=True)
    user_id = Column(ForeignKey("user.user_id"), nullable=False, index=True)

    gallery = relationship("Gallery")
    user = relationship("User")
