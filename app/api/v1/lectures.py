from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api.deps import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.LectureResponse])
def read_lectures(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve all lectures.
    """
    lectures = crud.lecture.get_multi(db, skip=skip, limit=limit)
    return lectures


@router.post("", response_model=schemas.LectureResponse)
def create_lecture(*, db: Session = Depends(get_db), lecture_in: schemas.LectureCreate) -> Any:
    """
    Create new lectures.
    """
    lecture = crud.lecture.create(db, obj_in=lecture_in)
    return lecture


@router.put("", response_model=schemas.LectureResponse)
def update_lecture(*, db: Session = Depends(get_db), lecture_in: schemas.LectureUpdate) -> Any:
    """
    Update existing lectures.
    """
    lecture = crud.lecture.get(db, model_id=lecture_in.id)
    if not lecture:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The lecture with this ID does not exist in the system.",
        )
    lecture = crud.lecture.update(db, db_obj=lecture, obj_in=lecture_in)
    return lecture


@router.delete("", response_model=schemas.Message)
def delete_lecture(*, db: Session = Depends(get_db), id: int) -> Any:
    """
    Delete existing lecture.
    """
    lecture = crud.lecture.get(db, model_id=id)
    if not lecture:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The lecture with this ID does not exist in the system.",
        )
    crud.lecture.remove(db, model_id=lecture.id)
    return {"message": f"Lecture with ID = {id} deleted."}
