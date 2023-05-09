from typing import Optional, List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.lecture import Lecture
from app.schemas import LectureCreate, LectureUpdate


class CRUDLecture(CRUDBase[Lecture, LectureCreate, LectureUpdate]):
    # Declare model specific CRUD operation methods.
    pass


lecture = CRUDLecture(Lecture)
