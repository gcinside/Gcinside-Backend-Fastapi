from db.base import Base
from sqlalchemy import Column, DateTime, ForeignKey, Text, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TINYINT


class PostComment(Base):
    __tablename__ = "post_comment"

    comment_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    author_id = Column(ForeignKey("user.user_id"), nullable=False, index=True)
    post_id = Column(ForeignKey("post.post_id"), nullable=False, index=True)
    comment_content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    is_child_comment = Column(TINYINT(1), nullable=True)
    parent_comment_id = Column(Integer, nullable=True)

    author = relationship("User")
    post = relationship("Post")
