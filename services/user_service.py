from repo.user_repo import UserRepo
import logging 
from sqlalchemy.orm import Session
from fastapi import HTTPException 
from schemas.user_schemas import UserCreate, UserUpdate 
import uuid

logger = logging.getLogger(__name__) 
class UserService:
    def __init__(self, db_session: Session):
        self.user_repo: UserRepo = UserRepo(db_session)

    def create_user(self, user_info: UserCreate):
        if self.user_repo.user_exists_by_email(user_info.email):
            raise HTTPException(status_code=400, detail="Email already registered")
        
        return self.user_repo.create_user(**user_info.model_dump(exclude_unset=True)) 

    def update_user(self, user_id: uuid.UUID, user_info: UserUpdate):
        user = self.user_repo.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return self.user_repo.update_user(user_id, **user_info.model_dump(exclude_unset=True))

    def delete_user(self, user_id: uuid.UUID):
        user = self.user_repo.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return self.user_repo.delete_user(user_id)

    def get_user_by_id(self, user_id: uuid.UUID):
        user = self.user_repo.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def get_user_by_email(self, email: str):
        user = self.user_repo.get_user_by_email(email)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    