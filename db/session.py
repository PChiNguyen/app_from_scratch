from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 
from core.config import settings 
from sqlalchemy import event
from sqlalchemy.engine import Engine
import logging     
logger= logging.getLogger(__name__)   
engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, echo= True)

Sessionlocal= sessionmaker(bind= engine, autocommit= False, autoflush= False) 

def get_db():
    db= Sessionlocal()
    try:
        yield db
    finally:
        db.close()
try: 
    with engine.connect() as connection:
        logger.info("Database connection successful")
except Exception as e:
    logger.error(f"Database connection failed: {e}") 

try: 
    db= Sessionlocal()   
    logger.info("Session created successfully")
except Exception as e:
    logger.error(f"Session creation failed: {e}") 
    


