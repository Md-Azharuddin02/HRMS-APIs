from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeResponse,
    EmployeeUpdate
)
from app.services import employee_service

router = APIRouter()


@router.post("/", response_model=EmployeeResponse, status_code=201)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return employee_service.create_employee(db, employee)


@router.get("/", response_model=List[EmployeeResponse])
def list_employees(db: Session = Depends(get_db)):
    return employee_service.get_employees(db)


@router.delete("/{employee_id}", status_code=200)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    return employee_service.delete_employee(db, employee_id)


@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    return employee_service.update_employee_service(db, employee_id, employee)