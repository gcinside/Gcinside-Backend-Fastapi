from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_sqlalchemy import db
from utils.verify_token import verify_token
from utils.get_payload_value import get_payload_value
from schemas.report import UserReportIn, UserReportOut
from models.user import User
from models.user_report import UserReport


router = APIRouter()


@router.post("", response_model=UserReportOut)
async def create_report(user_report: UserReportIn, token: str = Depends(verify_token)):

    email = get_payload_value(token, "sub")
    reporter = db.session.query(User).filter_by(user_email=email).first()
    target = db.session.query(User).filter_by(user_id=user_report.userid).first()

    if target.user_id == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    report = db.session.query(UserReport).filter_by(reporter_id=reporter.user_id, target_id=target.user_id).first()

    if report != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already reported")

    db.session.add(
        UserReport(reporter_id=reporter.user_id, target_id=target.user_id, reason=user_report.reason, is_block=False)
    )
    db.session.commit()

    return {"message": "Report success"}
