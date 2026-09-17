from services.student_service import StudentService
import pytest 
from schemas.student_schemas import StudentCreate
from sqlalchemy.orm import Session 
from db.models.classroom import Classroom 
from db.models.student import Student, OverallAim
from fastapi import HTTPException
import logging
import uuid 
from core.exceptions import ResourceNotFoundError

logger = logging.getLogger(__name__)

@pytest.fixture 
def student_service(db_session: Session):
    return StudentService(db_session) 

def test_create_student_success(student_service: StudentService, mock_classroom: Classroom):
    student = StudentCreate(name="John Doe", overall_aim=OverallAim.AIM_6_0, classroom_id=mock_classroom.id)
    created_student = student_service.create_student(student)
    assert created_student
    assert created_student.name == "John Doe"
    assert created_student.overall_aim == OverallAim.AIM_6_0

def test_create_student_failure(student_service: StudentService):
    student = StudentCreate(name="John Doe", overall_aim=OverallAim.AIM_6_0, classroom_id=uuid.uuid4())
    with pytest.raises(ResourceNotFoundError) as exc_info:
        student_service.create_student(student)
    assert exc_info.value.status_code == 404
    logger.error(f"Failed to create student: {exc_info.value}")

