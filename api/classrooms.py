from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.deps import get_current_teacher, get_db
from db.models.user import User
from schemas.classroom_schemas import (
    ClassroomCreate,
    ClassroomRead,
    ClassroomUpdate,
)
from services.classroom_service import ClassroomService

router = APIRouter()


@router.post("", response_model=ClassroomRead, status_code=status.HTTP_201_CREATED)
def create_classroom(
    *,
    classroom_info: ClassroomCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher),
):
    """Creates a new classroom owned by the authenticated teacher."""
    service = ClassroomService(db)
    return service.create_classroom(classroom_info)


@router.get("", response_model=List[ClassroomRead])
def read_classrooms(
    *,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher),
):
    """Lists all classrooms with pagination."""
    service = ClassroomService(db)
    classrooms = service.get_all_classrooms(skip=skip, limit=limit)
    if not classrooms:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No classrooms found",
        )
    return classrooms


@router.get("/teacher/{teacher_id}", response_model=List[ClassroomRead])
def read_classrooms_by_teacher_id(
    *,
    teacher_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher),
):
    """Fetches all classrooms belonging to a specific teacher UUID."""
    service = ClassroomService(db)
    classrooms = service.get_classroom_by_teacher_id(teacher_id)
    if not classrooms:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher does not have any classrooms",
        )
    return classrooms


@router.get("/{classroom_id}", response_model=ClassroomRead)
def read_classroom(
    *,
    classroom_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher),
):
    """Fetches a single classroom by its UUID."""
    service = ClassroomService(db)
    classroom = service.get_classroom_by_id(classroom_id)
    if not classroom:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Classroom not found",
        )
    return classroom


@router.put("/{classroom_id}", response_model=ClassroomRead)
def update_classroom(
    *,
    classroom_id: UUID,
    classroom_info: ClassroomUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher),
):
    """Updates classroom details by UUID."""
    service = ClassroomService(db)
    classroom = service.update_classroom(classroom_id, classroom_info)
    if not classroom:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Classroom not found",
        )
    return classroom


@router.delete("/{classroom_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_classroom(
    *,
    classroom_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher),
):
    """Deletes a classroom by UUID."""
    service = ClassroomService(db)
    classroom = service.delete_classroom(classroom_id)
    if not classroom:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Classroom not found",
        )
    return None