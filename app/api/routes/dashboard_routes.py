from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services import dashboard_service

router = APIRouter()


@router.get("/")
def dashboard_stats(db: Session = Depends(get_db)):
    return dashboard_service.get_dashboard_stats(db)