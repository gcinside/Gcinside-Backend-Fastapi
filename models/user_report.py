from db.base import Base
from sqlalchemy import Column, ForeignKey, Text, Integer
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship


class UserReport(Base):
    __tablename__ = "user_report"

    report_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    reporter_id = Column(ForeignKey("user.user_id"), nullable=False, index=True)
    target_id = Column(ForeignKey("user.user_id"), nullable=False, index=True)
    reason = Column(Text, nullable=False)
    is_block = Column(TINYINT(1), nullable=False)

    reporter = relationship("User", primaryjoin="UserReport.reporter_id == User.user_id")
    target = relationship("User", primaryjoin="UserReport.target_id == User.user_id")
