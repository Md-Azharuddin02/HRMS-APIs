from sqlalchemy.orm import Session
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate


def create_employee(db: Session, employee: EmployeeCreate):

    db_employee = Employee(
        employee_id=employee.employee_id,
        full_name=employee.full_name,
        email=employee.email,
        department=employee.department
    )

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


def get_employee_by_email(db: Session, email: str):
    return db.query(Employee).filter(Employee.email == email).first()


def get_employee_by_employee_id(db: Session, employee_id: str):
    return db.query(Employee).filter(Employee.employee_id == employee_id).first()


def get_employee_by_id(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()


def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Employee).offset(skip).limit(limit).all()


def delete_employee(db: Session, employee_id: int):

    employee = get_employee_by_id(db, employee_id)

    if not employee:
        return None

    db.delete(employee)
    db.commit()

    return employee


def update_employee(db: Session, employee: Employee, data: EmployeeUpdate):

    employee.full_name = data.full_name
    employee.email = data.email
    employee.department = data.department

    db.commit()
    db.refresh(employee)

    return employee