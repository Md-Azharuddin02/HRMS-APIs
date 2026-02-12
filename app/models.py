from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey, UniqueConstraint, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
import enum


class AttendanceStatus(str, enum.Enum):
    PRESENT = "Present"
    ABSENT = "Absent"


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    # Business ID (HR ID)
    employee_id = Column(String, unique=True, nullable=False, index=True)

    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    department = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    attendance_records = relationship(
        "Attendance",
        back_populates="employee",
        cascade="all, delete"
    )


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)

    # Foreign key → Employee.id
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)

    date = Column(Date, nullable=False)
    status = Column(Enum(AttendanceStatus), nullable=False)

    employee = relationship("Employee", back_populates="attendance_records")

    __table_args__ = (
        UniqueConstraint("employee_id", "date", name="unique_employee_date"),
    )
