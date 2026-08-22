import pytest  
from api import auth 
import logging 
from db.models.user import User 
from fastapi.testclient import TestClient 

logger = logging.getLogger(__name__) 

def test_login_success(mock_user: User, client: TestClient):
    # Must use "username" key for OAuth2PasswordRequestForm
    login_data = {"username": mock_user.email, "password": 'password'}
    
    # Use data= for form data (use json= if sending raw JSON)
    response = client.post("/api/auth/login", data= login_data)
    if response.status_code != 200:
        print(f"DEBUG: {response.json()}")
    
    assert response.status_code == 200



def test_read_user_me(client: TestClient):
    response = client.get("/api/auth/me")
    assert response.status_code == 200   