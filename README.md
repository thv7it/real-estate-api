# 🏠 Real Estate API

Backend REST API for a real estate agency built with **FastAPI** and **PostgreSQL**.

The project implements user authentication, role-based authorization, property management, and database migrations.

## 🚀 Features

- User registration
- User login
- JWT authentication
- Password hashing with Argon2
- Role-based access (`client` / `admin`)
- Get current authenticated user
- Create real estate properties
- View all active properties
- View property by ID
- Update properties
- Soft delete properties
- Input validation with Pydantic
- Database migrations with Alembic
- Automatic API documentation with Swagger

## 🛠 Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- PyJWT
- Argon2
- Uvicorn

## 📁 Project Structure

```text
real-estate-api/
├── alembic/
│   └── versions/
│
├── app/
│   ├── models/
│   │   ├── property.py
│   │   └── user.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   ├── properties.py
│   │   └── users.py
│   │
│   ├── schemas/
│   │   ├── property.py
│   │   └── user.py
│   │
│   ├── config.py
│   ├── database.py
│   ├── dependencies.py
│   ├── enums.py
│   ├── main.py
│   └── security.py
│
├── .env.example
├── .gitignore
├── alembic.ini
└── requirements.txt
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/thv7it/real-estate-api.git
cd real-estate-api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file based on `.env.example`:

```env
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=real_estate_db

SECRET_KEY=your_secret_key
```

### 5. Create the PostgreSQL database

Create a database named:

```text
real_estate_db
```

### 6. Apply database migrations

```bash
alembic upgrade head
```

### 7. Run the application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 📚 API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## 🔐 Authentication

The API uses JWT Bearer authentication.

After registration, log in through:

```text
POST /auth/login
```

The server returns an access token. Use this token to access protected endpoints.

Some property management operations are restricted to users with the `admin` role.

## 🏘 Main Endpoints

| Method | Endpoint | Description | Access |
|---|---|---|---|
| POST | `/auth/register` | Register a new user | Public |
| POST | `/auth/login` | Login and receive JWT | Public |
| GET | `/users/me` | Get current user | Authenticated |
| GET | `/properties` | Get active properties | Public |
| GET | `/properties/{property_id}` | Get property by ID | Public |
| POST | `/properties` | Create property | Admin |
| PATCH | `/properties/{property_id}` | Update property | Admin |
| DELETE | `/properties/{property_id}` | Soft delete property | Admin |

## 🔒 Security

- Passwords are never stored in plain text.
- Passwords are hashed using Argon2.
- Authentication is implemented with JWT access tokens.
- Administrative endpoints are protected by role-based authorization.
- Sensitive configuration is stored in environment variables.
- `.env` is excluded from Git.

## 👩‍💻 Author

**Tansuluu Satyshova**

Backend development learning project.