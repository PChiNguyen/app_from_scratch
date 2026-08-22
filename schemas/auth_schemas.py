from pydantic import BaseModel  
from typing import Optional, List 
from uuid import UUID  


# the digital card 
class Token(BaseModel):
    access_token: str
    token_type: str  = "bearer"  


# the chip inside the digital card 
class TokenPayload(BaseModel):
    sub: Optional[UUID] = None     # subject , user id
    role: Optional[str] = None      # user role  
    scopes: List[str] =[] # a list of things a user can do , if something is not in the list 
#                            then the user is not allowed to do it 
    exp: Optional[int] = None   # expiration time     