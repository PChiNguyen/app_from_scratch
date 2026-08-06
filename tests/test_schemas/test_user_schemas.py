from schemas.user_schemas import UserCreate, UserUpdate, UserRead
import pytest
import logging 

logger = logging.getLogger(__name__) 

def test_user_create():
    try: 
        user = UserCreate(
            email = 'NkYg5@example.com',
            password = 'password',
            role = 'STUDENT'
        )
        logger.info(f"UserCreate instance created successfully: {user}") 
    except Exception as e:
        logger.error(f"Error creating UserCreate instance: {e}") 
        pytest.fail(f"UserCreate instance creation failed: {e}")     