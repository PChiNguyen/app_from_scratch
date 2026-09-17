from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import ValidationError
from sqlalchemy.orm import Session

# Correct paths based on your file names
from db.session import get_db
from core.config import settings
from db.models.user import User, UserRole
from services.user_service import UserService 
from schemas.auth_schemas import TokenPayload    
from core.exceptions import ResourceNotFoundError 


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")     


def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme),
):  
    try: 
        payload= jwt.decode(token, 
                    settings.SECRET_KEY, 
                   algorithms=[settings.ALGORITHM])
        token_data= TokenPayload(**payload) 
    except (JWTError, ValidationError) as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                             detail=f"Could not validate credentials: {e}") 

    user = UserService(db).get_user_by_id(token_data.sub)
    if not user:
        raise ResourceNotFoundError
    return user



def get_current_teacher(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role not in [UserRole.TEACHER, UserRole.ADMIN]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have enough cuteness to perform this action"
        )
    return current_user
def get_current_student(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role not in [UserRole.STUDENT, UserRole.ADMIN]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action"
        )
    return current_user  

def get_current_admin(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action"
        )
    return current_user 


