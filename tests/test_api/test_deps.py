import uuid
from repo.user_repo import UserRepo  
import pytest 
from core.security import create_access_token 
from api.deps import get_current_user   
from fastapi import HTTPException      
from sqlalchemy.orm import Session    
from db.models. user import User 
import logging 
from core.exceptions import ResourceNotFoundError 

logger = logging.getLogger(__name__)


def test_get_current_user_success(db_session: Session, mock_user: User): 
    access_token = create_access_token(mock_user.id) 
    user= get_current_user(db_session, access_token)   
    assert user

def test_get_current_user_fail(db_session: Session): 
    access_token = create_access_token(uuid.uuid4()) 
    with pytest.raises(HTTPException) as e: 
        get_current_user(db_session, access_token)
    logger.error(f"Error getting current user: {e}")      
  