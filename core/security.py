from datetime import datetime, timedelta, timezone 
from typing import Optional, Union, Any 
from jose import jwt 
from passlib.context import CryptContext 
from core.config import settings    
import bcrypt 



def get_password_hash(password: str) -> str:
    #step 1: convert password to bytes
    pwd_bytes = password.encode('utf-8')
    #step 2: generate salt
    salt = bcrypt.gensalt()
    #step 3: hash password with salt 
    hashed_bytes = bcrypt.hashpw(pwd_bytes, salt)
    #step 4: convert hash to string
    return hashed_bytes.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str):
    #step 1: convert password to bytes
    pwd_bytes = plain_password.encode('utf-8')
    #step 2: convert hash to bytes
    hashed_bytes = hashed_password.encode('utf-8')
    #step 3: compare (bcrypt has a checkpw method)
    return bcrypt.checkpw(pwd_bytes, hashed_bytes)



# Creating the digical card  
def create_access_token(subject: Union[str, Any], expires_delta: Optional[timedelta] = None)->str:
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        # Pulls the default 'Backup' value from your config.py
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode =({"exp": expire,
                    "sub": str(subject)}) # 'exp' is the expiration date
                                        # 'sub' is the subject, usually the user id     
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    # the secret key makes sure 
    return encoded_jwt 