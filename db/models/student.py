import uuid
import enum
from typing import TYPE_CHECKING, List
from sqlalchemy import String, ForeignKey, UUID as SQLUUID, Enum as SQLEnum 
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base

if TYPE_CHECKING:
    from db.models.classroom import Classroom
    from db.models.student_score import StudentScore


class OverallAim(float, enum.Enum):
    AIM_6_0 = 6.0
    AIM_7_0 = 7.0
    AIM_8_0 = 8.0
    AIM_9_0 = 9.0


class Student(Base): 
    __tablename__ = 'students' 

    id: Mapped[uuid.UUID] = mapped_column(SQLUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    overall_aim: Mapped[OverallAim] = mapped_column(SQLEnum(OverallAim), nullable=False) 
    classroom_id: Mapped[uuid.UUID] = mapped_column(SQLUUID(as_uuid=True), ForeignKey('classrooms.id'), nullable=False) 

    classroom: Mapped["Classroom"] = relationship('Classroom', back_populates='students')
    student_scores: Mapped[List["StudentScore"]] = relationship('StudentScore', back_populates='student', cascade='all, delete-orphan')