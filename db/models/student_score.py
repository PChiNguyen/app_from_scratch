from sqlalchemy import Column, Integer, Float, String, ForeignKey, CheckConstraint, UUID as SQLUUID, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates  
from db.base import Base
from typing import TYPE_CHECKING
import uuid
import math 
from enum import Enum 
if TYPE_CHECKING:
    from db.models.student import Student
class band_score(Enum):
    band6 = 6.0
    band6_5 = 6.5
    band7 = 7.0
    band7_5 = 7.5

class StudentScore(Base):
    __tablename__ = 'student_score'
    id: Mapped[uuid.UUID] = mapped_column( SQLUUID(as_uuid=True),default=uuid.uuid4,primary_key=True)
    student_id: Mapped[uuid.UUID] = mapped_column( SQLUUID(as_uuid=True),ForeignKey('students.id'))
    score: Mapped[band_score] = mapped_column(SQLEnum(band_score), nullable= True)
    skill_id: Mapped[int] = mapped_column(ForeignKey('skills.id')) 

    skills = relationship('SkillModel', back_populates='student_score')
    student = relationship('Student', back_populates='student_scores')
    

