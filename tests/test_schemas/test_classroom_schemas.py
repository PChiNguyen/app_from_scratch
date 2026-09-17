from schemas.classroom_schemas import ClassroomCreate 
import pytest
import logging
import uuid 

logger = logging.getLogger(__name__)

def test_classroom_create(): 
    try: 
        classroom = ClassroomCreate(name='haha', teacher_id=uuid.uuid4()) 
        logger.info(f"ClassroomCreate instance created successfully: {classroom}") 
    except Exception as e: 
        logger.error(f"Error creating ClassroomCreate instance: {e}") 
        pytest.fail(f"ClassroomCreate instance creation failed: {e}") 