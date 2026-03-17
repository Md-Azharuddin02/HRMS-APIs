from sqlalchemy.orm import Session
from app.models.attendance import Attendance
from app.schemas.attendance import AttendanceCreate


def create_attendance(db: Session, attendance: AttendanceCreate):
    db_attendance = Attendance(
        employee_id=attendance.employee_id,
        date=attendance.date,
        status=attendance.status
    )

    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)

    return db_attendance


def get_attendance_by_employee(db: Session, employee_id: int):
    return db.query(Attendance).filter(
        Attendance.employee_id == employee_id
    ).all()


def get_attendance_by_employee_and_date(db: Session, employee_id: int, date):
    return db.query(Attendance).filter(
        Attendance.employee_id == employee_id,
        Attendance.date == date
    ).first()


def get_all_attendance(db: Session):
    return db.query(Attendance).all()