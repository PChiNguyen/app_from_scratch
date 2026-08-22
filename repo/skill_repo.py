from db.models.skill import SkillModel
from sqlalchemy.orm import Session 
import uuid 


class SkillRepo:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_skill(self, **kwargs):
        skill = SkillModel(**kwargs)
        try: 
            self.db_session.add(skill)
            self.db_session.commit()
            self.db_session.refresh(skill) 
            return skill
        except Exception as e:
            self.db_session.rollback()
            raise e   

    def get_all(self):
        return self.db_session.query(SkillModel).all()
    def get_by_id(self, skill_id: int):
        return self.db_session.query(SkillModel).filter(SkillModel.id == skill_id).first()
    def get_by_name(self, skill_name: str):
        return self.db_session.query(SkillModel).filter(SkillModel.name == skill_name).first() 

    