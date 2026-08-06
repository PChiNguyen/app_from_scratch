from db.models.skill import SkillModel, Skill 
import pytest  
import logging
from sqlalchemy.orm import Session  

logger = logging.getLogger(__name__) 


def test_create_skill(db_session: Session):
    try:
        skill = SkillModel(name=Skill.READING)
        db_session.add(skill)
        db_session.commit()
        logger.info(f"Skill created successfully: {skill.name}")
    except Exception as e:
        db_session.rollback()
        logger.error(f"Failed to create skill: {e}")
        pytest.fail(f"Failed to create skill: {e}")