from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date

from app.models.employee import Employee
from app.models.attendance import Attendance


def get_dashboard_stats(db: Session):

    total_employees = db.query(func.count(Employee.id)).scalar()

    today = date.today()

    present_today = db.query(func.count(Attendance.id)).filter(
        Attendance.date == today,
        Attendance.status == "present"
    ).scalar()

    absent_today = db.query(func.count(Attendance.id)).filter(
        Attendance.date == today,
        Attendance.status == "absent"
    ).scalar()

    return {
        "total_employees": total_employees,
        "present_today": present_today,
        "absent_today": absent_today
    }