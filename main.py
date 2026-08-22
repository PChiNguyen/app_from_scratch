import logging
import os
import traceback
from datetime import datetime, timezone

from fastapi import APIRouter, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

'''from core.exceptions import AppException
# 🟢 IMPORT REUSABLE REDIS CLIENT (From core/redis.py)
from core.redis import redis_client'''

# ==========================================
# 1. DATABASE & MODEL IMPORTS
# ==========================================
from db.base import Base
from db.models import (user, student, classroom, skill, student_score)
from db.session import engine

# ==========================================
# 2. ROUTER IMPORTS
# ==========================================
from api import (auth, deps) 

# Initialize database tables (MVP approach)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Ielts exam api",
    description="Whatever",
    version="2.0.0")


app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])  

