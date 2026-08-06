from pydantic import BaseModel, ConfigDict, Field, EmailStr, field_validator
from db.models.student import Student 
from uuid import UUID 
from typing import Optional
import re     


class StudentBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    overall_aim: float = Field(..., ge=6.0, le=9.0)
    classroom_id: UUID  


class StudentCreate(StudentBase):
    pass    

class StudentUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    overall_aim: Optional[float] = Field(None, ge=6.0, le=9.0)
    classroom_id: Optional[UUID]

class StudentRead(StudentBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)

    

