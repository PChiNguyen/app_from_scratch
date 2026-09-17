import pytest

from core.exceptions import ResourceNotFoundError
from services.student_score_service import StudentScoreService
from schemas.student_score_schemas import StudentScoreCreate
from sqlalchemy.orm import Session
from db.models.skill import SkillModel
from db.models.student import Student 
from db.models.student_score import StudentScore, BandScore 
from fastapi import HTTPException 


@pytest.fixture
def student_score_service(db_session: Session):
    return StudentScoreService(db_session)

def test_create_student_score_success(student_score_service: StudentScoreService, mock_student: Student, mock_skill: SkillModel):
    student_score = StudentScoreCreate(
        student_id=mock_student.id,
        score=BandScore.BAND_7_0,
        skill_id=mock_skill.id
    )
    created_student_score = student_score_service.create_student_score(student_score)
    assert created_student_score

def test_create_student_score_failure(student_score_service: StudentScoreService, mock_student: Student):
    student_score = StudentScoreCreate(
        student_id=mock_student.id,
        score=BandScore.BAND_7_0,
        skill_id=1000
    )
    with pytest.raises(ResourceNotFoundError) as e:
        student_score_service.create_student_score(student_score)
    assert e.value.status_code == 404 