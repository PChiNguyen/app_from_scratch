from db.models.user import User, UserRole   
from sqlalchemy.orm import Session
import uuid 
from sqlalchemy import exists 
from core.security import get_password_hash




class UserRepo:
    def __init__(self, db_session: Session):
        self.db_session: Session = db_session

    def create_user(self, **kwargs):
        data_in = kwargs
        data_in['password'] = get_password_hash(data_in['password'])
        try: 
            user = User(**kwargs)
            self.db_session.add(user)
            self.db_session.commit()
            self.db_session.refresh(user) 
            return user    
        except Exception as e:
            self.db_session.rollback()
            return None 

    def get_user_by_email(self, email: str):
        return self.db_session.query(User).filter(User.email == email).first()  

    def get_user_by_id(self, user_id: uuid.UUID):
        return self.db_session.query(User).filter(User.id == user_id).first()

    def user_exists_by_email(self, email: str):
        return self.db_session.query(exists().where(User.email == email)).scalar()

    def update_user(self, user_id: uuid.UUID, **kwargs):
        user = self.db_session.query(User).filter(User.id == user_id).first()
        if user:
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
                else:
                    raise AttributeError(f"User model has no attribute '{key}'")
        try:
            self.db_session.commit()
            self.db_session.refresh(user)   
            return user 
        except Exception as e:
            self.db_session.rollback()
            return None  

        

                    
        

    def delete_user(self, user_id: uuid.UUID):
        user = self.db_session.query(User).filter(User.id == user_id).first()
        if user:
            try: 
                self.db_session.delete(user)
                self.db_session.commit()
                return True
            except Exception as e:
                self.db_session.rollback()
                return False
        

    