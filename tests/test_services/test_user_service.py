import pytest 
import logging
from services.user_service import UserService 
from sqlalchemy.orm import Session 
from schemas.user_schemas import UserCreate, UserUpdate
from db.models.user import User, UserRole 
from repo.user_repo import UserRepo
from fastapi import HTTPException 

logger = logging.getLogger(__name__)

@pytest.fixture
def user_service(db_session: Session):
    return UserService(db_session) 
def test_create_user(user_service: UserService):
    info= UserCreate( email = 'NkYg5@example.com', password = 'password', role = UserRole.STUDENT)
    user = user_service.create_user(info)
    assert user 
    assert user.email == 'NkYg5@example.com'
    assert user.password == 'password'
    assert user.role == UserRole.STUDENT
    logging.info(f"User created successfully: {user.email}")


def test_create_user_fail(user_service: UserService,mock_user: User):
    info= UserCreate( email = mock_user.email, password = 'password', role = UserRole.STUDENT)
    with pytest.raises(HTTPException) as e:
        user = user_service.create_user(info)
    logger.error(f"Error creating user: {e}")   

    