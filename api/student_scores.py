from services.student_score_service import StudentScoreService 
from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session 
from db.models.user import User 
from api.deps import get_db, get_current_teacher 
from schemas.student_score_schemas import StudentScoreCreate, StudentScoreUpdate, StudentScoreResponse   
import uuid 
from typing import List



router = APIRouter() 

@router.post("", response_model= StudentScoreResponse, status_code=status.HTTP_201_CREATED)
def create_student_score(
    *,
    student_score_info: StudentScoreCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher),
):
    service = StudentScoreService(db)
    return service.create_student_score(student_score_info, current_user.id)

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

@router.get('/{skill_id}', response_model=List[StudentScoreResponse])
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

@router.get('/{student_id}', response_model=List[StudentScoreResponse])
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