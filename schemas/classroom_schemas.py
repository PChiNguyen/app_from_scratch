from pydantic import BaseModel, ConfigDict, Field, field_validator
from db.models.classroom import Classroom   
from uuid import UUID 
from typing import Optional
import re  



class ClassroomBase(BaseModel): 
    name: str = Field(..., min_length=1, max_length=255)
    teacher_id: UUID   


class ClassroomCreate(ClassroomBase): 
    pass 

class ClassroomUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    teacher_id: Optional[UUID]        

class ClassroomRead(ClassroomBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)      