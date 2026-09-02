from services.student_service import StudentService 
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.deps import get_current_teacher, get_db
from schemas.student_schemas import StudentCreate, StudentRead, StudentUpdate 
from db.models.user import User 
from typing import List 
import uuid 



router = APIRouter() 

@router.post("", response_model=StudentRead, status_code=status.HTTP_201_CREATED)
def create_student(
    *,
    student_info: StudentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher),
):
    service = StudentService(db)
    return service.create_student(student_info, current_user.id) 

@router.get("", response_model=List[StudentRead])
def read_all_students(
    *,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher),
):
    service = StudentService(db)
    return service.get_all_students()    

@router.get('classroom/{classroom_id}', response_model=List[StudentRead])
def read_students_by_classroom_id(
    *,
    classroom_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher),
):
    service = StudentService(db)
    return service.get_student_by_classroom_id(classroom_id)


@router.get("/{student_id}", response_model=StudentRead)
def read_student(
    *,
    student_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher),
):
    service = StudentService(db)
    return service.get_student_by_id(student_id)

@router.put("/{student_id}", response_model=StudentRead)
def update_student(
    *,
    student_id: uuid.UUID,
    student_info: StudentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher),
):
    service = StudentService(db)
    return service.update_student(student_id, student_info)   

@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(
    *,
    student_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher),
):
    service = StudentService(db)
    return service.delete_student(student_id)

