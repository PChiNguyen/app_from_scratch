from repo.student_repo import StudentRepo 
from repo.classroom_repo import ClassroomRepo 
from schemas.student_schemas import StudentCreate, StudentUpdate 
from sqlalchemy.orm import Session     
from fastapi import HTTPException 
import uuid


class StudentService:
    def __init__(self, db_session: Session):
        self.student_repo = StudentRepo(db_session) 
        self.classroom_repo = ClassroomRepo(db_session) 


    def create_student(self, student: StudentCreate):
        classroom = self.classroom_repo.get_classroom_by_id(student.classroom_id)
        if not classroom:
            raise HTTPException(status_code=404, detail="Classroom not found")
        return self.student_repo.create_student(**student.model_dump(exclude_unset=True))
    def get_all_students(self):
        return self.student_repo.get_all_students()

    def get_student_by_id(self, student_id: uuid.UUID):
        if not self.student_repo.get_student_by_id(student_id):
            raise HTTPException(status_code=404, detail="Student not found")
        return self.student_repo.get_student_by_id(student_id)

    def get_student_by_name(self, name: str):
        return self.student_repo.get_student_by_name(name)

    def get_student_by_classroom_id(self, classroom_id: uuid.UUID):
        if not self.classroom_repo.get_classroom_by_id(classroom_id):
            raise HTTPException(status_code=404, detail="Classroom not found")
        return self.student_repo.get_student_by_classroom_id(classroom_id)

    def update_student(self, student_id: uuid.UUID, student: StudentUpdate):
        if not self.student_repo.get_student_by_id(student_id):
            raise HTTPException(status_code=404, detail="Student not found")
        return self.student_repo.update_student(student_id, **student.model_dump(exclude_unset=True))

    def delete_student(self, student_id: uuid.UUID):
        if not self.student_repo.get_student_by_id(student_id):
            raise HTTPException(status_code=404, detail="Student not found")
        return self.student_repo.delete_student(student_id)