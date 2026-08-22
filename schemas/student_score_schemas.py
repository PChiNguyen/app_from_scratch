from pydantic import BaseModel, ConfigDict, Field, EmailStr, field_validator
from db.models.student_score import StudentScore, band_score 
from uuid import UUID 
from typing import Optional
import re  

class StudentScoreBase(BaseModel):
    student_id: UUID
    skill_id: int 
    score: band_score 

class StudentScoreCreate(StudentScoreBase):
    pass

class StudentScoreUpdate(StudentScoreBase):
    skill_id: Optional[int] = None
    score: Optional[band_score] = None

class StudentScoreResponse(StudentScoreBase):
    id: UUID      

    model_config = ConfigDict(from_attributes=True)  
