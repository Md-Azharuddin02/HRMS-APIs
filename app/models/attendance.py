from sqlalchemy import Column, Integer, Date, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from app.core.database import Base


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False
    )

    date = Column(Date, nullable=False)

    status = Column(String, nullable=False)

    employee = relationship(
        "Employee",
        back_populates="attendance_records"
    )

    __table_args__ = (
        UniqueConstraint("employee_id", "date", name="unique_employee_date"),
    )