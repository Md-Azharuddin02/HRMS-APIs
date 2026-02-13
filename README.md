<div align="center">

# 🎯 HRMS Lite – Backend API

### A Modern, Lightweight Human Resource Management System

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)

**Built with FastAPI and PostgreSQL for efficient employee management and attendance tracking**

[Features](#-features) • [Installation](#️-installation) • [API Documentation](#-api-endpoints) • [Database Schema](#-database-schema)

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 👥 Employee Management
- ✅ Create new employees
- ✅ View all employees
- ✅ Delete employees
- ✅ Unique employee code validation
- ✅ Email uniqueness validation
- ✅ Proper HTTP status handling

</td>
<td width="50%">

### 📅 Attendance Management
- ✅ Mark attendance (Present/Absent)
- ✅ Prevent duplicate entries
- ✅ View attendance by employee
- ✅ Relational data integrity
- ✅ Date-based tracking
- ✅ Foreign key constraints

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

<div align="center">

| Technology | Purpose | Version |
|:----------:|:-------:|:-------:|
| **Python** | Backend Language | 3.10+ |
| **FastAPI** | Web Framework | Latest |
| **PostgreSQL** | Database | Latest |
| **SQLAlchemy** | ORM | Latest |
| **Pydantic** | Data Validation | Latest |
| **Uvicorn** | ASGI Server | Latest |

</div>

---

## 📊 Database Schema

### 🏢 Employees Table
```sql
┌─────────────┬──────────┬────────────────────┐
│   Field     │   Type   │       Notes        │
├─────────────┼──────────┼────────────────────┤
│ id          │ Integer  │ Primary Key        │
│ employee_id │ String   │ Unique Code        │
│ full_name   │ String   │ Required           │
│ email       │ String   │ Unique             │
│ department  │ String   │ Required           │
│ created_at  │ DateTime │ Auto-generated     │
└─────────────┴──────────┴────────────────────┘
```

### 📝 Attendance Table
```sql
┌─────────────┬──────────┬──────────────────────────────┐
│   Field     │   Type   │          Notes               │
├─────────────┼──────────┼──────────────────────────────┤
│ id          │ Integer  │ Primary Key                  │
│ employee_id │ Integer  │ FK → employees.id            │
│ date        │ Date     │ Required                     │
│ status      │ Enum     │ Present / Absent             │
└─────────────┴──────────┴──────────────────────────────┘

⚠️ Unique Constraint: (employee_id, date)
```

---

## ⚙️ Installation

### 📋 Prerequisites

- Python 3.10 or higher
- PostgreSQL installed and running
- Git

### 🚀 Quick Start

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/HRMS-Backend.git
cd HRMS-Backend
```

#### 2️⃣ Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

#### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4️⃣ Setup Environment Variables

Create a `.env` file in the root directory:
```env
DATABASE_URL=postgresql://username:password@localhost:5432/hrms
```

#### 5️⃣ Run the Server
```bash
uvicorn app.main:app --reload
```

#### 🎉 Access the Application

- **API Server**: `http://localhost:8000`
- **Interactive Docs**: `http://localhost:8000/docs`
- **Alternative Docs**: `http://localhost:8000/redoc`
- **Live Demo**: [https://hrms-api-uwae.onrender.com/docs](https://hrms-api-uwae.onrender.com/docs)

---

## 🌐 API Endpoints

### 👥 Employee Endpoints

<table>
<tr>
<th>Method</th>
<th>Endpoint</th>
<th>Description</th>
<th>Status Codes</th>
</tr>

<tr>
<td><code>POST</code></td>
<td><code>/employees/</code></td>
<td>Create new employee</td>
<td><code>201</code> <code>409</code> <code>422</code></td>
</tr>

<tr>
<td><code>GET</code></td>
<td><code>/employees/</code></td>
<td>Retrieve all employees</td>
<td><code>200</code></td>
</tr>

<tr>
<td><code>DELETE</code></td>
<td><code>/employees/{id}</code></td>
<td>Delete employee by ID</td>
<td><code>204</code> <code>404</code></td>
</tr>
</table>

### 📅 Attendance Endpoints

<table>
<tr>
<th>Method</th>
<th>Endpoint</th>
<th>Description</th>
<th>Status Codes</th>
</tr>

<tr>
<td><code>POST</code></td>
<td><code>/attendance/</code></td>
<td>Mark employee attendance</td>
<td><code>201</code> <code>404</code> <code>409</code></td>
</tr>

<tr>
<td><code>GET</code></td>
<td><code>/attendance/{employee_id}</code></td>
<td>Get attendance records</td>
<td><code>200</code> <code>404</code></td>
</tr>
</table>

---

## 🎯 Design Decisions

<div align="center">

| Decision | Rationale |
|:---------|:----------|
| **Surrogate Primary Keys** | Using auto-incrementing IDs for better relationship management |
| **Business Employee Code** | Stored as `employee_id` (string) for flexibility |
| **SQLAlchemy Relationships** | Cascade delete for data integrity |
| **Unique Constraints** | Prevent duplicate attendance entries |
| **RESTful Design** | Proper HTTP status codes and resource naming |
| **Pydantic Validation** | Automatic request/response validation |

</div>

---

## ⚠️ Current Limitations

- 🔐 No authentication/authorization
- 📄 No pagination support
- 🔍 Limited filtering capabilities
- 👤 Single admin assumption
- 📊 No analytics dashboard

---

## 🚀 Future Roadmap

<table>
<tr>
<td>

### Phase 1
- [ ] JWT Authentication
- [ ] Role-based access control
- [ ] Pagination support
- [ ] Advanced filtering

</td>
<td>

### Phase 2
- [ ] Date range filtering
- [ ] Analytics dashboard
- [ ] Export functionality
- [ ] Email notifications

</td>
<td>

### Phase 3
- [ ] Docker support
- [ ] CI/CD pipeline
- [ ] Unit tests
- [ ] API versioning

</td>
</tr>
</table>

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Your Name**

- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/YOUR_PROFILE)

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

**Made with ❤️ using FastAPI and PostgreSQL**

</div>
