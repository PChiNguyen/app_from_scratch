from db.models.user import User, UserRole # Bây giờ nó sẽ hết lỗi
import pytest 
from sqlalchemy.exc import IntegrityError 
from sqlalchemy import text 
from db.models.user import User, UserRole  
from sqlalchemy.orm import Session
import logging 
import uuid 

logger = logging.getLogger(__name__) 


def test_create_user(db_session: Session):
    # 🟢 Generate a unique email using an 8-character random hex string
    random_hex = uuid.uuid4().hex[:8]
    unique_email = f"user_{random_hex}@example.com"

    try:
        user = User(
            email=unique_email,
            password='password',
            role=UserRole.STUDENT
        )
        db_session.add(user)
        db_session.commit()  
        logger.info(f"User created successfully: {user.email}")
    except Exception as e:
        db_session.rollback()  
        logger.error(f"Failed to create user: {e}")
        pytest.fail(f"Failed to create user: {e}")
    except Exception as e:
        db_session.rollback()  
        logger.error(f"Failed to create user: {e}")
        pytest.fail(f"Failed to create user: {e}")
