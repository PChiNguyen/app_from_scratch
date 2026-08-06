from pydantic import BaseModel, ConfigDict, Field, EmailStr, field_validator
from db.models.skill import SkillModel, Skill   
from uuid import UUID 
from typing import Optional
import re  

class SkillBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)

class SkillCreate(SkillBase):
    pass   
