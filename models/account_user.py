from sqlalchemy import Column, DateTime, String, Integer, Boolean
from db.base import Base


class AccountUser(Base):
    __tablename__ = "account_user"

    user_id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String(255), nullable=False)
    profile_image = Column(String(100), nullable=False, index=True)
    user_name = Column(String(20), nullable=False)
    join_date = Column(DateTime, nullable=False)
    is_superuser = Column(Boolean, nullable=False)
    is_staff = Column(Boolean, nullable=False)
