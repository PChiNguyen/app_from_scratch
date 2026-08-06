from db.models.student_score import StudentScore, band_score 
import pytest 
from sqlalchemy.orm import Session
import logging  
import uuid 
from db.models.student import Student
from db.models.skill import SkillModel

logger = logging.getLogger(__name__)


def test_create_student_score(db_session: Session, mock_student: Student, mock_skill: SkillModel):
    try:
        student_score = StudentScore(student_id=mock_student.id, score=band_score.band7, skill_id=mock_skill.id)
        db_session.add(student_score)
        db_session.commit()
        logger.info(f"Student score created successfully: {student_score.student_id}")
    except Exception as e:
        db_session.rollback()
        logger.error(f"Failed to create student score: {e}")
        pytest.fail(f"Failed to create student score: {e}")