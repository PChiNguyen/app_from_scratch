import pytest
from api import classrooms 
import logging 
from db.models.user import User 
from fastapi.testclient import TestClient   
from core.exceptions import DatabaseValidationError, ResourceNotFoundError 
from schemas.classroom_schemas import ClassroomCreate   
import uuid       
from db.models.classroom import Classroom

logger = logging.getLogger(__name__) 

def test_create_classroom_fail(client: TestClient):
    # 1. Prepare request payload
    classroom_data = ClassroomCreate(name='haha', teacher_id=uuid.uuid4())
    
    # 2. Execute POST request
    response = client.post(
        "/api/classrooms", 
        json=classroom_data.model_dump(mode="json")
    ) 
    
    # 3. Parse the JSON dictionary returned by exception handler
    response_data = response.json()
    
    # 4. Extract and print AI suggestion
    ai_suggestion = response_data.get("ai_suggestion")
    print(f"\n🤖 [AI SUGGESTION]: {ai_suggestion}")
    
    # 5. Assert expected response state
    assert response.status_code == 404
    assert ai_suggestion is not None



    
