from repo.skill_repo import SkillRepo 
from db.models.skill import SkillModel, Skill 
from schemas.skill_schemas import SkillCreate
from sqlalchemy.orm import Session


class SkillService():
    def __init__(self, db_session: Session):
        self.repo = SkillRepo(db_session=db_session)

    def create_skill(self, skill_info: SkillCreate):
        return self.repo.create_skill(**skill_info.model_dump(exclude_unset=True)) 

    def get_all_skills(self):
        return self.repo.get_all()

    def get_skill_by_id(self, skill_id: int):
        return self.repo.get_by_id(skill_id)    

    def get_skill_by_name(self, skill_name: str):
        return self.repo.get_by_name(skill_name) 