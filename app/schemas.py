from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from enum import Enum


class AttendanceStatus(str, Enum):
    PRESENT = "Present"
    ABSENT = "Absent"


# -------------------
# Employee Schemas
# -------------------

class EmployeeBase(BaseModel):
    employee_id: str
    full_name: str
    email: EmailStr
    department: str


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeResponse(EmployeeBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# -------------------
# Attendance Schemas
# -------------------

class AttendanceBase(BaseModel):
    employee_id: int   # This refers to Employee.id (NOT business employee_id)
    date: date
    status: AttendanceStatus


class AttendanceCreate(AttendanceBase):
    pass


class AttendanceResponse(AttendanceBase):
    id: int

    class Config:
        from_attributes = True
