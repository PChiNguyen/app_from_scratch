from repo.student_repo import StudentRepo 
import pytest 
import logging 
from sqlalchemy.orm import Session  
from schemas.student_schemas import StudentCreate, StudentUpdate 
from db.models.student import Student, OverallAim  
from db.models.classroom import Classroom 
import uuid 
logger = logging.getLogger(__name__) 

@pytest.fixture
def student_repo(db_session: Session):
    return StudentRepo(db_session) 


def test_create_student(student_repo: StudentRepo, mock_classroom: Classroom): 
    student_info = StudentCreate(name="John Doe", overall_aim=OverallAim.AIM_6_0, classroom_id=mock_classroom.id).model_dump(exclude_unset=True)
    student = student_repo.create_student(**student_info) 
    assert student 
    assert student.name == "John Doe"
    assert student.overall_aim == OverallAim.AIM_6_0


def test_get_student_by_id(student_repo: StudentRepo, mock_student: Student):
    student = student_repo.get_student_by_id(mock_student.id) 
    assert student 
    assert student.id ==    mock_student.id 

def test_get_student_by_name(student_repo: StudentRepo, mock_student: Student):
    student = student_repo.get_student_by_name(mock_student.name) 
    assert student, "Student not found" 
    assert student.name == mock_student.name



