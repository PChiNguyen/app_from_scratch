from pydantic import BaseModel, ConfigDict, Field, field_validator
from db.models.classroom import Classroom, Type
from uuid import UUID 
from typing import Optional
import re  



class ClassroomBase(BaseModel): 
    name: Type 
    teacher_id: UUID   


class ClassroomCreate(ClassroomBase): 
    pass 

class ClassroomUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    teacher_id: Optional[UUID] = Field(None)             

class ClassroomRead(ClassroomBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)      