from schemas.student_schemas import StudentCreate, StudentUpdate, StudentRead
import pytest   
import logging 
from db.models.student import Student, OverallAim
import uuid 

logger = logging.getLogger(__name__)

def test_student_create():
    try:
        student = StudentCreate(
            name = 'John Doe',
            overall_aim = OverallAim.AIM_6_0,
            classroom_id = uuid.uuid4()
        )
        logger.info(f"StudentCreate instance created successfully: {student}")
    except Exception as e:
        logger.error(f"Error creating StudentCreate instance: {e}")
        pytest.fail(f"StudentCreate instance creation failed: {e}")