import logging
import pytest
from sqlalchemy.orm import Session

from db.models.classroom import Classroom
from db.models.skill import Skill, SkillModel
from db.models.student import Student
from db.models.student_score import StudentScore, band_score
from repo.grading_repo import GradingRepo

logger = logging.getLogger(__name__)


# ==========================================
# 1. OPTIMIZED FIXTURES
# ==========================================




@pytest.fixture
def grading_repo(db_session: Session) -> GradingRepo:
    """Instantiates the repository with the active test database session."""
    return GradingRepo(db_session)


# ==========================================
# 2. TEST CASES WITH EXPLICIT ASSERTIONS
# ==========================================

def test_get_classroom_overall_band_scores(
    grading_repo: GradingRepo,
    mock_classroom: Classroom,
    mock_student: Student,
    mock_full_student_scores: list[StudentScore]
):
    """
    Verifies that classroom-wide overall band scores calculated by SQL 
    match expected averages and record counts.
    """
    results = grading_repo.get_classroom_overall_band_scores(mock_classroom.id)

    # 1. Ensure data was returned
    assert results is not None
    assert len(results) == 1

    # 2. Verify exact values
    student_score = results[0]
    assert student_score.student_id == mock_student.id
    assert float(student_score.overall) == 6.25
    assert student_score.completed_tests == 4

    logger.info(f"Classroom overall score calculated: {student_score.overall}")


def test_get_student_overall_band_score(
    grading_repo: GradingRepo,
    mock_classroom: Classroom,
    mock_student: Student,
    mock_full_student_scores: list[StudentScore]
):
    """
    Verifies that querying a specific student's overall band score 
    filters accurately and calculates the correct average score.
    """
    results = grading_repo.get_student_overall_band_score(
        mock_classroom.id, 
        mock_student.id
    )

    # 1. Ensure single record returned for target student
    assert results is not None
    assert len(results) == 1

    # 2. Verify accurate calculation and properties
    student_score = results[0]
    assert student_score.student_id == mock_student.id
    assert float(student_score.overall) == 6.25
    assert student_score.completed_tests == 4

    logger.info(f"Student overall score fetched: {student_score}")