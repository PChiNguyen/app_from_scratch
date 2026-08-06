from db.models.student import Student, ovr_aim
import pytest 
import logging
from sqlalchemy.orm import Session 
import uuid 
from db.models.classroom import Classroom

logger = logging.getLogger(__name__)


def test_create_student(db_session: Session, mock_classroom: Classroom):
    try:
        student = Student(name="John Doe", overall_aim=ovr_aim.aim1, classroom_id=mock_classroom.id)
        db_session.add(student)
        db_session.commit()
        logger.info(f"Student created successfully: {student.name}")
    except Exception as e:
        db_session.rollback()
        logger.error(f"Failed to create student: {e}")
        pytest.fail(f"Failed to create student: {e}")