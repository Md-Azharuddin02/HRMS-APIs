from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, crud

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post("/", response_model=schemas.EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    created_employee = crud.create_employee(db, employee)

    if not created_employee:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Employee with this Employee ID or Email already exists."
        )

    return created_employee


@router.get("/", response_model=list[schemas.EmployeeResponse])
def get_all_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_employee(db, id)

    if deleted is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found."
        )

