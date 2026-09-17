from repo.skill_repo import SkillRepo 
from db.models.skill import Skill, SkillModel
from db.session import Sessionlocal   

from db.base import Base 
from core.config import settings
from db.models.user import User, UserRole
from db.models.classroom import Classroom
from db.models.student import Student, OverallAim
from db.models.skill import SkillModel 
from db.models.student_score import StudentScore, BandScore 





def create_skill():
    db_session = Sessionlocal()
    if SkillRepo(db_session).get_by_name(Skill.READING):
        print(f"❌ Skill '{Skill.READING}' already exists in the database.")
        return  
    skill = SkillRepo(db_session).create_skill(name=Skill.READING)
    print(f"✅ Skill '{skill.name}' created successfully with ID: {skill.id}") 



if __name__ == "__main__": 
    create_skill()