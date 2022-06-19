from sqlalchemy import Column, DateTime, ForeignKey, String, Integer, Text
from sqlalchemy.orm import relationship
from db.base import Base

class PostPost(Base):
    __tablename__ = 'post_post'

    post_id = Column(Integer, primary_key=True, index=True)
    author_id = Column(ForeignKey('account_user.user_id'), nullable=False, index=True)
    gallery_id = Column(ForeignKey('gallery_gallery.gallery_id'), nullable=False, index=True)
    post_title = Column(String(120), nullable=False)
    post_content = Column(Text, nullable=False, index=True)
    post_image = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)

    author = relationship('AccountUser')
    gallery = relationship('GalleryGallery')