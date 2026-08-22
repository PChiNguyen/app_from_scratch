from pydantic import BaseModel, ConfigDict, Field 
import uuid  

class OverallBandRead(BaseModel):
    student_id: uuid.UUID
    student_name: str
    overall: float
    completed_tests: int
    