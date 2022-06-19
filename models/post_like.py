from sqlalchemy import Column, ForeignKey,Integer,Boolean
from sqlalchemy.orm import relationship
from db.base import Base


class PostLike(Base):
    __tablename__ = 'post_like'

    like_id = Column(Integer, primary_key=True, index=True)
    post_id = Column(ForeignKey('post_post.post_id'), nullable=False, index=True)
    user_id = Column(ForeignKey('account_user.user_id'), nullable=False, index=True)
    like_type = Column(Boolean, nullable=False)

    post = relationship('PostPost')
    user = relationship('AccountUser')