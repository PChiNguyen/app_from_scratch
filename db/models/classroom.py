import uuid
from typing import TYPE_CHECKING, List
from sqlalchemy import String, ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base

if TYPE_CHECKING:
    from db.models.user import User
    from db.models.student import Student


class Classroom(Base): 
    __tablename__ = 'classrooms' 

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    teacher_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False) 

    teacher: Mapped["User"] = relationship('User', back_populates='classrooms') 
    students: Mapped[List["Student"]] = relationship('Student', back_populates='classroom', cascade='all, delete-orphan')