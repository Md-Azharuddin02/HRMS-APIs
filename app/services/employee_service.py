from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.schemas.employee import EmployeeCreate
import app.repositories.employee_repo as employee_repository


def create_employee(db: Session, employee: EmployeeCreate):

    existing_email = employee_repository.get_employee_by_email(
        db, employee.email
    )

    if existing_email:
        raise HTTPException(
            status_code=409,
            detail="Employee with this email already exists"
        )

    existing_emp_id = employee_repository.get_employee_by_employee_id(
        db, employee.employee_id
    )

    if existing_emp_id:
        raise HTTPException(
            status_code=409,
            detail="Employee ID already exists"
        )

    return employee_repository.create_employee(db, employee)


def get_employees(db: Session):
    return employee_repository.get_employees(db)


def delete_employee(db: Session, employee_id: int):

    employee = employee_repository.get_employee_by_id(db, employee_id)

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee_repository.delete_employee(db, employee_id)


def update_employee_service(db: Session, employee_id: int, data):

    employee = employee_repository.get_employee_by_id(db, employee_id)

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee_repository.update_employee(db, employee, data)