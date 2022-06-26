from db.base import Base
from sqlalchemy import Column, DateTime, String, Integer
from sqlalchemy.dialects.mysql import TINYINT


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_email = Column(String(100), nullable=False, index=True)
    profile_image = Column(String(100), nullable=False)
    user_name = Column(String(100), nullable=False)
    join_date = Column(DateTime, nullable=False)
    is_staff = Column(TINYINT(1), nullable=False)
