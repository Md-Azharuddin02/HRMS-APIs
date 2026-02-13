# HRMS Lite – Backend API

A lightweight Human Resource Management System (HRMS Lite) backend built using **FastAPI** and **PostgreSQL**.

This API handles employee management and attendance tracking with proper validation, error handling, and RESTful design principles.

---

## 🚀 Tech Stack

- Python 3.10+
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic
- Uvicorn

---

## 📦 Features

### Employee Management
- Create employee
- View all employees
- Delete employee
- Unique employee code & email validation
- Proper HTTP status handling (201, 204, 404, 409, 422)

### Attendance Management
- Mark attendance (Present / Absent)
- Prevent duplicate attendance for same employee & date
- View attendance by employee
- Relational integrity using Foreign Keys

---

## 🗂 Database Schema

### Employees Table
| Field        | Type     | Notes              |
|--------------|----------|-------------------|
| id           | Integer  | Primary Key        |
| employee_id  | String   | Unique Code        |
| full_name    | String   | Required           |
| email        | String   | Unique             |
| department   | String   | Required           |
| created_at   | DateTime | Auto generated     |

### Attendance Table
| Field        | Type     | Notes                             |
|--------------|----------|------------------------------------|
| id           | Integer  | Primary Key                        |
| employee_id  | Integer  | Foreign Key → employees.id         |
| date         | Date     | Required                           |
| status       | Enum     | Present / Absent                   |

Unique Constraint:
- (employee_id, date)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/HRMS-Backend.git
cd HRMS-Backend

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate  # Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Setup Environment Variables

Create .env file:

DATABASE_URL=postgresql://username:password@localhost:5432/hrms

5️⃣ Run Server
uvicorn app.main:app --reload


API Docs available at:

https://hrms-api-uwae.onrender.com/docs

🌐 API Endpoints
Employees
Method	Endpoint	Description
POST	/employees/	Create employee
GET	/employees/	Get all employees
DELETE	/employees/{id}	Delete employee
Attendance
Method	Endpoint	Description
POST	/attendance/	Mark attendance
GET	/attendance/{employee_id}	Get employee attendance
🧠 Design Decisions

Used surrogate primary key (id) for relationships.

Business employee code stored as employee_id (string).

Used SQLAlchemy relationships with cascade delete.

Used UniqueConstraint to prevent duplicate attendance.

Implemented proper HTTP status codes.

🚧 Limitations

No authentication (single admin assumption)

No pagination

No filtering support

📌 Future Improvements

Pagination

Filtering attendance by date

Dashboard statistics

JWT Authentication

Dockerization

