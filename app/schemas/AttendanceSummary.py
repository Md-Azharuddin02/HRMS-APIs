class AttendanceSummary(BaseModel):
    employee_id: int
    present_days: int
    absent_days: int