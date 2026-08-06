from pydantic import BaseModel, ConfigDict, Field, EmailStr, field_validator
from db.models.student_score import StudentScore, band_score 
from uuid import UUID 
from typing import Optional
import re  

class StudentScoreBase(BaseModel):
    student_id: UUID
    skill_id: UUID
    score: band_score 

class StudentScoreCreate(StudentScoreBase):
    pass

class StudentScoreUpdate(StudentScoreBase):
    skill_id: Optional[UUID]
    score: Optional[band_score] 

class StudentScoreResponse(StudentScoreBase):
    id: UUID      
