from pydantic import BaseModel


class UserReportIn(BaseModel):
    userid: int
    reason: str

    class Config:
        schema_extra = {"example": {"userid": "1", "reason": "마음에 안듦"}}


class UserReportOut(BaseModel):
    message: str

    class Config:
        schema_extra = {"example": {"message": "Report success"}}


class ViewReportListOut(BaseModel):
    report_list: list

    class Config:
        schema_extra = {
            "example": {
                "report_list": [
                    {"report_id": "1", "reporter_id": "1", "target_id": "1", "reason": "마음에 안듦", "is_block": "False"}
                ]
            }
        }
