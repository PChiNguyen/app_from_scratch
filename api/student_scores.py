from typing import List
import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.deps import get_current_teacher, get_db
from db.models.user import User
from schemas.student_score_schemas import (
    StudentScoreCreate,
    StudentScoreResponse,
    StudentScoreUpdate,
)
from services.student_score_service import StudentScoreService

router = APIRouter()


@router.post("", response_model=StudentScoreResponse, status_code=status.HTTP_201_CREATED)
def create_student_score(
    *,
    student_score_info: StudentScoreCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher),
):
    service = StudentScoreService(db)
    return service.create_student_score(student_score_info)


# 1. Get score by Score ID (UUID)
@router.get('/{student_score_id}', response_model=StudentScoreResponse)
def read_student_score(
    *,
    student_score_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher),
):
    service = StudentScoreService(db)
    student_score = service.get_student_score_by_id(student_score_id)
    if not student_score:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student score not found",
        )
    return student_score


# 2. Added '/skill/' prefix to avoid collision with UUID route
@router.get('/skill/{skill_id}', response_model=List[StudentScoreResponse])
def read_student_scores_by_skill_id(
    *,
    skill_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher),
):
    service = StudentScoreService(db)
    student_scores = service.get_student_scores_by_skill_id(skill_id)
    if not student_scores:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No student scores found for this skill",
        )
    return student_scores


# 3. Added '/student/' prefix to avoid collision with other routes
@router.get('/student/{student_id}', response_model=List[StudentScoreResponse])
def read_student_scores_by_student_id(
    *,
    student_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher),
):
    service = StudentScoreService(db)
    student_scores = service.get_student_scores_by_student_id(student_id)
    if not student_scores:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No student scores found for this student",
        )
    return student_scores


@router.put('/{student_score_id}', response_model=StudentScoreResponse)
def update_student_score(
    *,
    student_score_id: uuid.UUID,
    student_score_info: StudentScoreUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher),
):
    service = StudentScoreService(db)
    student_score = service.update_student_score(student_score_id, student_score_info)
    if not student_score:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student score not found",
        )
    return student_score


@router.delete('/{student_score_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_student_score(
    *,
    student_score_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher),
):
    service = StudentScoreService(db)
    student_score = service.delete_student_score(student_score_id)
    if not student_score:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student score not found",
        )
    return None