import uuid
from sqlalchemy.orm import Session

from core.exceptions import ResourceNotFoundError
from repo.classroom_repo import ClassroomRepo
from repo.grading_repo import GradingRepo
from repo.student_repo import StudentRepo


class GradingService:
    def __init__(self, db: Session):
        self.grading_repo = GradingRepo(db)
        self.classroom_repo = ClassroomRepo(db)
        self.student_repo = StudentRepo(db)

    def get_classroom_overall_band_scores(self, classroom_id: uuid.UUID):
        if not self.classroom_repo.get_classroom_by_id(classroom_id):
            raise ResourceNotFoundError(message="Classroom not found")
        return self.grading_repo.get_classroom_overall_band_scores(classroom_id)

    def get_student_overall_band_score(self, classroom_id: uuid.UUID, student_id: uuid.UUID):
        if not self.classroom_repo.get_classroom_by_id(classroom_id):
            raise ResourceNotFoundError(message="Classroom not found")
        if not self.student_repo.get_student_by_id(student_id):
            raise ResourceNotFoundError(message="Student not found")
        return self.grading_repo.get_student_overall_band_score(classroom_id, student_id)