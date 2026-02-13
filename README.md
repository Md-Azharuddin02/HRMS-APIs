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
