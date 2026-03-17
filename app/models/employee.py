from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

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