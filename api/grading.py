from services.grading_service import GradingService  
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.deps import get_db, get_current_teacher 
from schemas.grading_schemas import OverallBandRead 
from typing import List  
from db.models.user import User 
import uuid 


router = APIRouter() 

@router.get("/classroom/{classroom_id}", response_model=List[OverallBandRead])
def read_classroom_overall_band_scores(*,classroom_id: uuid.UUID,db: Session = Depends(get_db), current_user: User = Depends(get_current_teacher)):
    service = GradingService(db)
    scores= service.get_classroom_overall_band_scores(classroom_id) 
    if not scores:
        raise HTTPException(status_code=404, detail="No scores found for this classroom")
    return scores

@router.get("/student/{student_id}", response_model=List[OverallBandRead])
def read_student_overall_band_scores(*,classroom_id: uuid.UUID, student_id: uuid.UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_teacher)):
    service = GradingService(db)
    score= service.get_student_overall_band_score(classroom_id, student_id)
    if not score:
        raise HTTPException(status_code=404, detail="No scores found for this student")
    return score