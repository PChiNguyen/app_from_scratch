from pydantic import BaseModel, ConfigDict, Field, EmailStr, field_validator
from db.models.student import Student 
from uuid import UUID 
from typing import Optional
import re     
from db.models.student import OverallAim 


class StudentBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    overall_aim: OverallAim
    classroom_id: UUID  


class StudentCreate(StudentBase):
    pass    

class StudentUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    overall_aim: Optional[OverallAim] = Field(None)
    classroom_id: Optional[UUID] = Field(None)

class StudentRead(StudentBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)

    

