import pytest 
from services.grading_service import GradingService
from sqlalchemy.orm import Session
from db.models.classroom import Classroom
from db.models.student import Student 
from db.models.student_score import StudentScore
from db.models.skill import SkillModel 
from fastapi import HTTPException
import uuid 
from core.exceptions import ResourceNotFoundError

@pytest.fixture
def grading_service(db_session: Session):
    return GradingService(db_session)

def test_get_classroom_overall_band_scores(grading_service: GradingService, mock_classroom: Classroom,
                                            mock_full_student_scores: list[StudentScore],
                                            mock_skills: dict[str, SkillModel]):
    classroom_overall_band_scores = grading_service.get_classroom_overall_band_scores(mock_classroom.id)
    assert classroom_overall_band_scores

def test_get_classroom_overall_band_scores_fails(grading_service: GradingService):
    with pytest.raises(ResourceNotFoundError) as exc_info:
        grading_service.get_classroom_overall_band_scores(uuid.uuid4())