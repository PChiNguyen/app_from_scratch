import uuid
import enum
from typing import TYPE_CHECKING, Optional
from sqlalchemy import ForeignKey, UUID as SQLUUID, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base

if TYPE_CHECKING:
    from db.models.student import Student
    from db.models.skill import SkillModel


class BandScore(float, enum.Enum):
    BAND_6_0 = 6.0
    BAND_6_5 = 6.5
    BAND_7_0 = 7.0
    BAND_7_5 = 7.5


class StudentScore(Base):
    __tablename__ = 'student_score'

    id: Mapped[uuid.UUID] = mapped_column(SQLUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id: Mapped[uuid.UUID] = mapped_column(SQLUUID(as_uuid=True), ForeignKey('students.id'), nullable=False)
    skill_id: Mapped[int] = mapped_column(ForeignKey('skills.id'), nullable=False)
    score: Mapped[Optional[BandScore]] = mapped_column(SQLEnum(BandScore), nullable=True)

    student: Mapped["Student"] = relationship('Student', back_populates='student_scores')
    skill: Mapped["SkillModel"] = relationship('SkillModel', back_populates='student_scores')