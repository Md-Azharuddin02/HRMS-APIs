from sqlalchemy.orm import Session
from app.repositories import dashboard_repo


def get_dashboard_stats(db: Session):
    return dashboard_repo.get_dashboard_stats(db)