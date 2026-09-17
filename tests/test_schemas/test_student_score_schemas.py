from schemas.student_score_schemas import StudentScoreCreate, StudentScoreUpdate
import pytest
import logging
from db.models.student_score import StudentScore, BandScore 
import uuid 

logger = logging.getLogger(__name__)    


def test_student_score_create():
    try: 
        student_score_create = StudentScoreCreate(student_id= uuid.uuid4(),
            skill_id=1,
            score=BandScore.BAND_7_0
        )
        logger.info(f"StudentScoreCreate instance created successfully: {student_score_create}") 
    except Exception as e:
        logger.error(f"Error creating StudentScoreCreate instance: {e}") 
        pytest.fail(f"StudentScoreCreate instance creation failed: {e}")