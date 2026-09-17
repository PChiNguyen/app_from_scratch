import enum
from typing import TYPE_CHECKING, List
from sqlalchemy import Integer, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base

if TYPE_CHECKING:
    from db.models.student_score import StudentScore


class Skill(str, enum.Enum):
    READING = 'reading'
    WRITING = 'writing'
    LISTENING = 'listening'
    SPEAKING = 'speaking' 


class SkillModel(Base):
    __tablename__ = 'skills'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[Skill] = mapped_column(SQLEnum(Skill), unique=True, nullable=False)

    student_scores: Mapped[List["StudentScore"]] = relationship('StudentScore', back_populates='skill')