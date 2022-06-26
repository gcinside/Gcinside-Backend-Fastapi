from db.base import Base
from sqlalchemy import Column, DateTime, ForeignKey, String, Text, Integer
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = "post"

    post_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    author_id = Column(ForeignKey("user.user_id"), nullable=False, index=True)
    gallery_id = Column(ForeignKey("gallery.gallery_id"), nullable=False, index=True)
    post_title = Column(String(100), nullable=False, index=True)
    post_content = Column(Text, nullable=False)
    post_image = Column(String(100), nullable=False, index=True)
    created_at = Column(DateTime, nullable=False)

    author = relationship("User")
    gallery = relationship("Gallery")
