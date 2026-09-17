from sqlalchemy.orm import Session

from core.exceptions import ResourceNotFoundError
from repo.skill_repo import SkillRepo
from schemas.skill_schemas import SkillCreate


class SkillService:
    def __init__(self, db_session: Session):
        self.repo = SkillRepo(db_session=db_session)

    def create_skill(self, skill_info: SkillCreate):
        return self.repo.create_skill(**skill_info.model_dump(exclude_unset=True))

    def get_all_skills(self):
        return self.repo.get_all()

    def get_skill_by_id(self, skill_id: int):
        skill = self.repo.get_by_id(skill_id)
        if not skill:
            raise ResourceNotFoundError(message=f"Skill with id {skill_id} not found")
        return skill

    def get_skill_by_name(self, skill_name: str):
        skill = self.repo.get_by_name(skill_name)
        if not skill:
            raise ResourceNotFoundError(message=f"Skill with name '{skill_name}' not found")
        return skill