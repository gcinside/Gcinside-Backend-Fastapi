from pydantic import BaseModel


class CreateCommentIn(BaseModel):
    content: str
    is_child_comment: bool = False
    parent_comment_id: int = None

    class Config:
        schema_extra = {"example": {"content": "댓글 내용"}}


class CreateCommentOut(BaseModel):
    message: str

    class Config:
        schema_extra = {"example": {"message": "Success to upload"}}


class ReadCommentOut(BaseModel):
    comment_list: list

    class Config:
        schema_extra = {
            "example": {
                "comment_list": [
                    {
                        "id": "1",
                        "author_id": "1",
                        "content": "댓글 내용",
                        "is_child_comment": False,
                        "parent_comment_id": None,
                    },
                    {
                        "id": "2",
                        "author_id": "1",
                        "content": "대댓글 내용",
                        "is_child_comment": True,
                        "parent_comment_id": "1",
                    },
                ]
            }
        }


class UploadCommentIn(BaseModel):
    content: str
    is_child_comment: bool
    paraent_comment_id: int


class UploadCommentOut(BaseModel):
    message: str

    class Config:
        schema_extra = {"example": {"message": "Success to upload comment"}}


class DeleteCommentOut(BaseModel):
    message: str

    class Config:
        schema_extra = {"example": {"message": "Success to delete comment"}}


class UpdateCommentIn(BaseModel):
    content: str

    class Config:
        schema_extra = {"example": {"content": "댓글 내용"}}


class UpdateCommentOut(BaseModel):
    message: str

    class Config:
        schema_extra = {"example": {"message": "Success to update comment"}}
