import pytest 
from services.classroom_service import ClassroomService
from schemas.classroom_schemas import ClassroomCreate 
from sqlalchemy.orm import Session 
from db.models.classroom import Type, Classroom 
from db.models.user import User 
from repo.classroom_repo import ClassroomRepo 
from repo.user_repo import UserRepo 
from fastapi import HTTPException
import uuid 
import logging
from core.exceptions import ResourceNotFoundError 

logger = logging.getLogger(__name__)

@pytest.fixture
def classroom_service(db_session: Session):
    return ClassroomService(db_session)

def test_create_classroom_sucess(classroom_service: ClassroomService, mock_user: User):
    classroom_info = ClassroomCreate(name=Type.number2_, teacher_id=mock_user.id)
    classroom = classroom_service.create_classroom(classroom_info)
    assert classroom.name == Type.number2_
    assert classroom.teacher_id == mock_user.id

def test_create_classroom_failure(classroom_service: ClassroomService, mock_user: User):
    classroom_info = ClassroomCreate(name=Type.number1_, teacher_id=uuid.uuid4())
    with pytest.raises(ResourceNotFoundError) as exc_info:
        classroom_service.create_classroom(classroom_info)
    assert exc_info.value.status_code == 404 
    logger.error(f"Failed to create classroom: {exc_info.value}") 