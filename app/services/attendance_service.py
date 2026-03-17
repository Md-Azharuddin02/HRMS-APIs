from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.schemas.attendance import AttendanceCreate
from app.repositories import attendance_repo, employee_repo


def mark_attendance(db: Session, attendance: AttendanceCreate):

    employee = employee_repo.get_employee_by_id(db, attendance.employee_id)

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    existing_record = attendance_repo.get_attendance_by_employee_and_date(
        db,
        attendance.employee_id,
        attendance.date
    )

    if existing_record:
        raise HTTPException(
            status_code=409,
            detail="Attendance already marked for this date"
        )

    return attendance_repo.create_attendance(db, attendance)    


from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories import attendance_repo, employee_repo


def get_employee_attendance(db: Session, employee_id: int):

    employee = employee_repo.get_employee_by_id(db, employee_id)

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return attendance_repo.get_attendance_by_employee(db, employee_id)


def get_all_attendance(db: Session):
    return attendance_repo.get_all_attendance(db)