from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.schemas.attendance import AttendanceCreate, AttendanceResponse
from app.services import attendance_service

router = APIRouter()


@router.post("/", response_model=AttendanceResponse, status_code=201)
def mark_attendance(attendance: AttendanceCreate, db: Session = Depends(get_db)):
    return attendance_service.mark_attendance(db, attendance)


@router.get("/", response_model=List[AttendanceResponse])
def get_all_attendance(db: Session = Depends(get_db)):
    return attendance_service.get_all_attendance(db)


@router.get("/{employee_id}", response_model=List[AttendanceResponse])
def get_employee_attendance(employee_id: int, db: Session = Depends(get_db)):
    return attendance_service.get_employee_attendance(db, employee_id)