from pydantic import BaseModel
from datetime import date
from typing import Literal


class AttendanceBase(BaseModel):
    employee_id: int
    date: date
    status: Literal["present", "absent"]


class AttendanceCreate(AttendanceBase):
    pass


class AttendanceResponse(AttendanceBase):
    id: int

    class Config:
        from_attributes = True