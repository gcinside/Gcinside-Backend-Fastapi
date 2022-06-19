from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text, Boolean
from sqlalchemy.orm import relationship
from db.base import Base


class PostComment(Base):
    __tablename__ = "post_comment"

    comment_id = Column(Integer, primary_key=True, index=True)
    author_id = Column(ForeignKey("account_user.user_id"), nullable=False, index=True)
    post_id = Column(ForeignKey("post_post.post_id"), nullable=False, index=True)
    comment_content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    is_child_comment = Column(Boolean, nullable=False)
    comment_group = Column(Integer)

    author = relationship("AccountUser")
    post = relationship("PostPost")
