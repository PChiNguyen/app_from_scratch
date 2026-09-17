from services.skill_service import SkillService
from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session 
from api.deps import get_db, get_current_admin 
from   db.models.user import User
from db.models.skill import Skill, SkillModel 



router = APIRouter()

@router.post("/system/init-skills", tags=["System Setup"])
def ininialize_skills(db: Session = Depends(get_db), current_user: User = Depends(get_current_admin)):

    skill_service = SkillService(db)
    skills= [Skill.SPEAKING, Skill.WRITING, Skill.LISTENING, Skill.READING]

    for skill in skills:
        if skill_service.get_skill_by_name(skill) is None:
            skill_service.create_skill(name=skill)

    return {"message": "Skills initialized successfully."}   