from db.base import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class PostLike(Base):
    __tablename__ = "post_like"

    like_id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(ForeignKey("post.post_id"), nullable=False, index=True)
    user_id = Column(ForeignKey("user.user_id"), nullable=False, index=True)
    like_type = Column(Integer, nullable=False)

    post = relationship("Post")
    user = relationship("User")
