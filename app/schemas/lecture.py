from typing import Optional

from pydantic import BaseModel


class LectureBase(BaseModel):
    id: Optional[int]
    title: Optional[str]
    description: Optional[str]


class LectureCreate(LectureBase):
    title: str
    description: str


class LectureUpdate(LectureBase):
    id: int
    pass


class LectureResponse(LectureBase):
    class Config:
        orm_mode = True
