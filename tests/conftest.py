import pytest
from sqlalchemy import create_engine, event 
from sqlalchemy.orm import sessionmaker, Session 
from core.config import settings 
from sqlalchemy.engine import Engine, Connection
import logging 
from db.base import Base
from db.models.classroom import Classroom
from db.models.skill import SkillModel
from db.models.student import Student
from db.models.user import User 



logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

@pytest.fixture
def mock_user(db_session: Session):
    from db.models.user import User, UserRole
    user = User(
        email = 'NkYg5@example.com',
        password = 'password',
        role = UserRole.STUDENT
    )
    db_session.add(user)
    db_session.commit()
    return user

@pytest.fixture
def mock_classroom(db_session: Session, mock_user: User):
    from db.models.classroom import Classroom, Type
    import uuid
    classroom = Classroom(
        name=Type.number1_,
        teacher_id=mock_user.id
    )
    db_session.add(classroom)
    db_session.commit()
    return classroom

@pytest.fixture
def mock_student(db_session: Session, mock_classroom: Classroom):
    from db.models.student import Student, ovr_aim
    import uuid
    student = Student(
        name="John Doe",
        overall_aim=ovr_aim.aim1,
        classroom_id=mock_classroom.id
    )
    db_session.add(student)
    db_session.commit()
    return student

@pytest.fixture
def mock_skill(db_session: Session):
    from db.models.skill import Skill, SkillModel
    skill = SkillModel(name=Skill.READING)
    db_session.add(skill)
    db_session.commit()
    return skill


@pytest.fixture
def mock_student_score(db_session: Session, mock_student: Student, mock_skill: SkillModel):
    from db.models.student_score import StudentScore, band_scoreEnum
    student_score = StudentScore(
        student_id=mock_student.id,
        score=band_scoreEnum.band7,
        skill_id=mock_skill.id
    )
    db_session.add(student_score)
    db_session.commit()
    return student_score























@pytest.fixture(scope='session')    
def engine():
    # Conditionally add connect_args based on database type
    connect_args = {}
    if "sqlite" in settings.SQLALCHEMY_DATABASE_URL.lower():
        connect_args = {"check_same_thread": False}
    
    _engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, connect_args=connect_args)
    
    # 1. Register the listener (DO NOT put yield here)
    @event.listens_for(_engine, "connect")
    def set_sqlite_pragma(dbapi_connection, connection_record):
        # Only execute PRAGMA for SQLite
        if "sqlite" in settings.SQLALCHEMY_DATABASE_URL.lower():
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.close()



    # 2. Import models so Base can see them
    from db.models.user import User
    from db.models.classroom import Classroom
    from db.models.student import Student
    from db.models.skill import Skill
    from db.models.student_score import StudentScore 

    # 3. Build the structure (This is outside the listener!)
    Base.metadata.create_all(bind=_engine)
    
    # 4. Give the engine to the tests
    yield _engine
    
    # 5. Cleanup
    Base.metadata.drop_all(bind=_engine)




@pytest.fixture(scope='function')
def db_session(engine:Engine):
    connection: Connection= engine.connect() 
    transaction= connection.begin()
    session_factory= sessionmaker(bind=connection)

    session:Session= session_factory()
    yield session
    session.close()
    transaction.rollback()
    connection.close()   