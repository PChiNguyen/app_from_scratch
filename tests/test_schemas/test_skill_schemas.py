from schemas.skill_schemas import SkillCreate
import pytest
import logging
from db.models.skill import SkillModel, Skill


logger = logging.getLogger(__name__)


def test_skill_create():
    try:
        skill = SkillCreate(name=Skill.READING)
        logger.info(f"Skill created successfully: {skill.name}")
    except Exception as e:
        logger.error(f"Failed to create skill: {e}")
        pytest.fail(f"Failed to create skill: {e}")