from pydantic import BaseModel, ConfigDict, Field, EmailStr, field_validator
from db.models.user import UserRole 
from uuid import UUID 
from typing import Optional
import re 

class UserBase(BaseModel):
    email: EmailStr
    role : UserRole 

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=255)

class UserUpdate(BaseModel):
    email: Optional[EmailStr]
    role: Optional[UserRole]
    password: Optional[str] = Field(None, min_length=8, max_length=255)  
class UserRead(UserBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)