from sqlalchemy import String, Integer, CheckConstraint, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates
from db.base import Base
from typing import TYPE_CHECKING
import enum

class Skill(enum.Enum):
    READING = 'reading'
    WRITING = 'writing'
    LISTENING = 'listening'
    SPEAKING = 'speaking' 

class SkillModel(Base):
    __tablename__ = 'skills'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[Skill] = mapped_column(SQLEnum(Skill), unique=True, nullable=False)

    student_score = relationship('StudentScore', back_populates='skills')
