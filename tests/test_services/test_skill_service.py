import pytest 
from services.skill_service import SkillService 
from schemas.skill_schemas import SkillCreate, Skill
from sqlalchemy.orm import Session

@pytest.fixture 
def skill_service(db_session: Session):
    return SkillService(db_session)
def test_create_skill_success(skill_service: SkillService):
    skill_info = SkillCreate(name= Skill.READING)
    skill = skill_service.create_skill(skill_info)
    assert skill.name == Skill.READING 
      