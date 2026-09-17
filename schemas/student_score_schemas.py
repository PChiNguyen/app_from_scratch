from pydantic import BaseModel, ConfigDict, Field, EmailStr, field_validator
from db.models.student_score import StudentScore, BandScore 
from uuid import UUID 
from typing import Optional
import re  

class StudentScoreBase(BaseModel):
    student_id: UUID
    skill_id: int 
    score: BandScore

class StudentScoreCreate(StudentScoreBase):
    pass

class StudentScoreUpdate(StudentScoreBase):
    skill_id: Optional[int] = None
    score: Optional[BandScore] = None

class StudentScoreResponse(StudentScoreBase):
    id: UUID      

    model_config = ConfigDict(from_attributes=True)  
