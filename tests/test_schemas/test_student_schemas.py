from schemas.student_schemas import StudentCreate, StudentUpdate, StudentRead
import pytest   
import logging 
from db.models.student import Student, ovr_aim 
import uuid 

logger = logging.getLogger(__name__)

def test_student_create():
    try:
        student = StudentCreate(
            name = 'John Doe',
            overall_aim = ovr_aim.aim1,
            classroom_id = uuid.uuid4()
        )
        logger.info(f"StudentCreate instance created successfully: {student}")
    except Exception as e:
        logger.error(f"Error creating StudentCreate instance: {e}")
        pytest.fail(f"StudentCreate instance creation failed: {e}")