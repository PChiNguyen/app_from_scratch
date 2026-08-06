import uuid
import re 
import enum 
from typing import TYPE_CHECKING
from sqlalchemy import String, ForeignKey, CheckConstraint,UUID as SQLUUID, Enum as SQLEnum 
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates 
from db.base import Base
if TYPE_CHECKING:
    from db.models.classroom import Classroom

class ovr_aim(enum.Enum):
    aim1 = 6.0
    aim2 = 7.0
    aim3 = 8.0
    aim4 = 9.0

class Student(Base): 
    __tablename__= 'students' 

    id: Mapped[uuid.UUID] = mapped_column(SQLUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    overall_aim: Mapped[ovr_aim] = mapped_column( SQLEnum(ovr_aim), nullable=False) 
    classroom_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('classrooms.id'), nullable=False) 

    classroom: Mapped['Classroom'] = relationship('Classroom', back_populates='students')
    student_scores = relationship('StudentScore', back_populates='student', cascade='all, delete-orphan') 