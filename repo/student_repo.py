from db.models.student import Student 
from sqlalchemy import func
from sqlalchemy.orm import Session 
import uuid 



class StudentRepo:
    def __init__(self, db_session: Session):
        self.db_session = db_session   

    def create_student(self, **kwargs):
        try:
            student = Student(**kwargs)
            self.db_session.add(student)
            self.db_session.commit()
            self.db_session.refresh(student) 
            return student
        except Exception as e:
            self.db_session.rollback()
            raise e 

    def get_all_students(self):
        return self.db_session.query(Student).all()

    def get_student_by_id(self, student_id):
        return self.db_session.query(Student).filter_by(id=student_id).first()

    def get_student_by_name(self, name:str):
        return self.db_session.query(Student).filter_by(name=name).first()

    def get_student_by_classroom_id(self, classroom_id):
        return self.db_session.query(Student).filter_by(classroom_id=classroom_id).all()

    def update_student(self, student_id, **kwargs):
        
        student = self.get_student_by_id(student_id)
        for key, value in kwargs.items():
            if hasattr(student, key):
                setattr(student, key, value)
        try: 
            self.db_session.commit()
            self.db_session.refresh(student) 
        except Exception as e:
            self.db_session.rollback()
            raise e


    def delete_student(self, student_id):
        try:
            student = self.get_student_by_id(student_id)
            self.db_session.delete(student)
            self.db_session.commit()
        except Exception as e:
            self.db_session.rollback()
            raise e
        