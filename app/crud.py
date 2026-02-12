from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import models, schemas


# ---------------------------
# EMPLOYEE CRUD
# ---------------------------

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(
        employee_id=employee.employee_id,
        full_name=employee.full_name,
        email=employee.email,
        department=employee.department
    )

    db.add(db_employee)
    try:
        db.commit()
        db.refresh(db_employee)
        return db_employee
    except IntegrityError:
        db.rollback()
        return None


def get_employees(db: Session):
    return db.query(models.Employee).order_by(models.Employee.id.asc()).all()


def get_employee_by_id(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


def delete_employee(db: Session, employee_id: int):
    employee = get_employee_by_id(db, employee_id)
    if not employee:
        return None

    db.delete(employee)
    db.commit()
    return employee


# ---------------------------
# ATTENDANCE CRUD
# ---------------------------

def create_attendance(db: Session, attendance: schemas.AttendanceCreate):
    db_attendance = models.Attendance(
        employee_id=attendance.employee_id,
        date=attendance.date,
        status=attendance.status
    )

    db.add(db_attendance)
    try:
        db.commit()
        db.refresh(db_attendance)
        return db_attendance
    except IntegrityError:
        db.rollback()
        return None


def get_attendance_by_employee(db: Session, employee_id: int):
    return (
        db.query(models.Attendance)
        .filter(models.Attendance.employee_id == employee_id)
        .order_by(models.Attendance.date.desc())
        .all()
    )
