from pydantic import BaseModel, EmailStr
from datetime import datetime


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

from pydantic import BaseModel, EmailStr

class EmployeeUpdate(BaseModel):
    name: str
    email: EmailStr
    department: str