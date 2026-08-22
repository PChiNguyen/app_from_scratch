from db.models.student_score import StudentScore  
from sqlalchemy.orm import Session
import uuid 
import logging 

logger = logging.getLogger(__name__) 



class StudentScoreRepo:
    def __init__(self, db_session: Session):
        self.db_session = db_session 

    def create_student_score(self, **kargs):
        try:
            student_score = StudentScore(**kargs)
            self.db_session.add(student_score)
            self.db_session.commit()
            self.db_session.refresh(student_score) 
            logger.info(f"Student score created successfully: {student_score.student_id}")
            return student_score
        except Exception as e:
            self.db_session.rollback()
            logger.error(f"Failed to create student score: {e}")    

    def get_student_scores_by_student_id(self, student_id: uuid.UUID):
        return self.db_session.query(StudentScore).filter_by(student_id=student_id).all()

    def get_student_scores_by_skill_id(self, skill_id: int):
        return self.db_session.query(StudentScore).filter_by(skill_id=skill_id).all()

    def get_student_score_by_id(self, student_score_id: uuid.UUID):
        return self.db_session.query(StudentScore).filter_by(id=student_score_id).first()

    def update_student_score(self, student_score_id: uuid.UUID, **kargs):
        
        student_score = self.get_student_score_by_id(student_score_id)
        if student_score:
            for key, value in kargs.items():
                if hasattr(student_score, key):
                    setattr(student_score, key, value)
            
        else:
            raise ValueError(f"Student score with id {student_score_id} not found")
        try:
            self.db_session.commit()
            self.db_session.refresh(student_score)
            logger.info(f"Student score updated successfully: {student_score.student_id}")
        except Exception as e:
            self.db_session.rollback()
    
            logger.error(f"Student score not found: {student_score_id}")

    def delete_student_score(self, student_score_id: uuid.UUID):
        try:
            student_score = self.get_student_score_by_id(student_score_id)
            if student_score:
                self.db_session.delete(student_score)
                self.db_session.commit()
                logger.info(f"Student score deleted successfully: {student_score.student_id}")
            else:
                logger.error(f"Student score not found: {student_score_id}")
        except Exception as e:
            self.db_session.rollback()
            logger.error(f"Failed to delete student score: {e}")