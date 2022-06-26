from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_sqlalchemy import db
from utils.verify_token import verify_token
from utils.get_payload_value import get_payload_value
from schemas.report import ViewReportListOut
from models.user import User
from models.user_report import UserReport


router = APIRouter()


@router.get("", response_model=ViewReportListOut)
async def read_report_list(token: str = Depends(verify_token)):

    email = get_payload_value(token, "sub")
    is_staff = db.session.query(User.is_staff).filter_by(user_email=email).first()

    if is_staff == False:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are unauthorized to make this request")

    result = []

    for report in db.session.query(UserReport).all():
        result.append(
            {
                "report_id": report.report_id,
                "reporter_id": report.reporter_id,
                "target_id": report.target_id,
                "reason": report.reason,
                "is_block": report.is_block,
            }
        )

    return {"report_list": result}
