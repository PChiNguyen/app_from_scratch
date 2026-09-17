from db.models.classroom import Classroom
import pytest
import logging 
from sqlalchemy.orm import Session 
import uuid

from db.models.user import User

logger = logging.getLogger(__name__)

def test_create_classroom(db_session: Session, mock_user: User):
    try:
        classroom = Classroom(name='haha', teacher_id=mock_user.id)
        db_session.add(classroom)
        db_session.commit()
        logger.info(f"Classroom created successfully: {classroom.name}")
    except Exception as e:
        db_session.rollback()
        logger.error(f"Failed to create classroom: {e}")
        pytest.fail(f"Failed to create classroom: {e}")