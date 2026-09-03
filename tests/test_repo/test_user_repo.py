from repo.user_repo import UserRepo 
import pytest 
import logging 
from sqlalchemy.orm import Session  
from schemas.user_schemas import UserCreate, UserUpdate 
from db.models.user import User , UserRole
import uuid 
logger = logging.getLogger(__name__)


@pytest.fixture 
def user_repo(db_session: Session):
    return UserRepo(db_session)  

def test_create_user(user_repo: UserRepo):
    random_hex = uuid.uuid4().hex[:8]
    unique_email = f"user_{random_hex}@example.com"
    info= UserCreate( email = unique_email, password = 'password', role = UserRole.STUDENT).model_dump(exclude_unset=True)
    user = user_repo.create_user(**info)    

    assert user
    assert user.email == unique_email
    assert user.role == UserRole.STUDENT
def test_get_user_by_email(user_repo: UserRepo, mock_user: User):
    user = user_repo.get_user_by_email(mock_user.email)
    assert user 

def test_get_user_by_id(user_repo: UserRepo, mock_user: User):
    user = user_repo.get_user_by_id(mock_user.id)
    assert user
def test_user_exists_by_email(user_repo: UserRepo, mock_user: User):
    assert user_repo.user_exists_by_email(mock_user.email) 

def test_update_user(user_repo: UserRepo, mock_user: User):
    info= UserUpdate(email = 'hahaha@gmail.com').model_dump(exclude_unset=True)
    user = user_repo.update_user(mock_user.id, **info)    
    assert user.email == 'hahaha@gmail.com' 

def test_delete_user(user_repo: UserRepo, mock_user: User):
    assert user_repo.delete_user(mock_user.id)    


