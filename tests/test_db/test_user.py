from db.models.user import User, UserRole # Bây giờ nó sẽ hết lỗi
import pytest 
from sqlalchemy.exc import IntegrityError 
from sqlalchemy import text 
from db.models.user import User, UserRole  
from sqlalchemy.orm import Session
import logging 

logger = logging.getLogger(__name__) 


def test_create_user(db_session: Session):
    try:
        user = User(
            email = 'NkYg5@example.com',
            password = 'password',
            role = UserRole.STUDENT
        )
        db_session.add(user)
        db_session.commit()  
        logger.info(f"User created successfully: {user.email}")
    except Exception as e:
        db_session.rollback()  
        logger.error(f"Failed to create user: {e}")
        pytest.fail(f"Failed to create user: {e}")
