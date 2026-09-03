import uuid 
import re 
import enum 
from sqlalchemy import String, ForeignKey, CheckConstraint,UUID, Enum as SQLEnum 

from sqlalchemy.orm import Mapped, mapped_column , relationship, validates

from db.base import Base
from typing import TYPE_CHECKING 

if TYPE_CHECKING: 
    from db.models.user import User 


class Type(enum.Enum):
    number1_ = 'number1'
    number2_ = 'number2'
    number3_ = 'number3'
    number4_ = 'number4' 

class Classroom(Base): 
    __tablename__= 'classrooms' 

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[Type] = mapped_column(SQLEnum(Type), unique=True, nullable=False)
    teacher_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('users.id'), nullable=False) 

    teacher: Mapped['User'] = relationship('User', back_populates='classrooms') 
    students = relationship('Student', back_populates='classroom', cascade='all, delete-orphan')


    @validates('name') 
    def validate_name(self, key, name): 
        if isinstance(name, str): 
            try:
                name= Type(name.lower()) 
                return name
            except ValueError:
                raise ValueError(f'{name} is not a valid classroom name')
        if isinstance(name, Type): 
            return name
        if not isinstance(name, Type): 
            raise TypeError(f'{name} should be of type {Type.number1_} or {Type.number2_} or {Type.number3_} or {Type.number4_}')    
            
             
            

            

