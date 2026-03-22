from fastapi import FastAPI
from app.core.config import settings
from app.core.database import Base, engine
from app.api.routes import employee_routes, attendance_routes
from fastapi import HTTPException
from app.utils.exceptions import http_exception_handler
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employee_routes.router, prefix="/employees", tags=["Employees"])
app.include_router(attendance_routes.router, prefix="/attendance", tags=["Attendance"])
app.add_exception_handler(HTTPException, http_exception_handler)
