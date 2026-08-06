from sqlalchemy.orm import Mapped, mapped_column, relationship, validates
from db.base import Base
import enum  
import uuid 
from sqlalchemy import String, Enum as SQLEnum, CheckConstraint, UUID, ForeignKey, Integer 


class UserRole(str, enum.Enum):
    ADMIN = 'admin'
    TEACHER = 'teacher'
    STUDENT = 'student'


class User(Base):
    __tablename__= 'users' 

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(SQLEnum(UserRole), nullable=False)

    classrooms = relationship('Classroom', back_populates='teacher', cascade='all, delete-orphan')


