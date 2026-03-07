# Medical Record Web Application

## Overview

This project is a **full-stack medical record web application** that allows users to submit and store their personal medical information.

Users can fill out a medical form through a web interface, and the data is stored securely in a PostgreSQL database.

The application consists of:

* Frontend: React-based web interface
* Backend: FastAPI REST API
* Database: PostgreSQL
* Containerization: Docker

---

## Technology Stack

Backend:

* Python
* FastAPI
* SQLAlchemy

Frontend:

* React
* Axios
* Bootstrap

Database:

* PostgreSQL

DevOps / Tools:

* Docker
* Git
* GitHub

---

## Project Structure

```
medical_website
│
├── backend
│   ├── app
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── database.py
│   │   └── schemas.py
│   │
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend
│   ├── src
│   │   ├── App.js
│   │   └── MedicalForm.js
│   │
│   ├── public
│   └── package.json
│
├── docker-compose.yml
└── README.md
```

---

# System Architecture

```
User Browser
     │
     ▼
React Frontend (Port 3000)
     │
     ▼
FastAPI Backend (Port 8000)
     │
     ▼
PostgreSQL Database (Port 5432)
```

---

# Prerequisites

Make sure the following software is installed:

* Python 3.10+
* Node.js
* npm
* Docker
* Git

---

# Clone the Repository

```
git clone https://github.com/<your-username>/medical-record-system.git
```

Navigate into the project folder:

```
cd medical-record-system
```

---

# Running the Backend

Navigate to the backend directory:

```
cd backend
```

Create virtual environment:

```
python -m venv venv
```

Activate virtual environment (Windows):

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run FastAPI server:

```
uvicorn app.main:app --reload
```

Backend will start at:

```
http://localhost:8000
```

API Documentation:

```
http://localhost:8000/docs
```

---

# Running the Frontend

Navigate to frontend folder:

```
cd frontend
```

Install dependencies:

```
npm install
```

Start React development server:

```
npm start
```

Frontend will run at:

```
http://localhost:3000
```

---

# Connecting to PostgreSQL

Default database configuration:

```
postgresql://admin:admin@db:5432/medicaldb
```

Database table will automatically be created when backend starts.

---

# Running with Docker (Recommended)

From the project root folder run:

```
docker-compose up --build
```

Docker will start:

* PostgreSQL container
* FastAPI backend container

Backend will be available at:

```
http://localhost:8000
```

---

# API Endpoint

### Create User Record

Endpoint:

```
POST /users
```

Example Request Body:

```
{
"name": "John Doe",
"email": "john@example.com",
"phone": "9999999999",
"address": "New York",
"medical_problem": "Diabetes"
}
```

---

# Verifying Data in PostgreSQL

Access database container:

```
docker exec -it postgres_container psql -U admin -d medicaldb
```

Run query:

```
SELECT * FROM users;
```

---

# Deployment

The application can be deployed using:

Backend:

* Render

Frontend:

* Vercel

Database:

* PostgreSQL (Render)

---

# Features

* Medical information form
* FastAPI REST API
* PostgreSQL database integration
* React frontend UI
* Docker containerization

---

# Future Enhancements

* User authentication (JWT)
* Medical history dashboard
* File upload for prescriptions
* Role-based access
* AI-powered symptom assistant

---

# Author

Satish Sindhe

---

# License

This project is for learning and demonstration purposes.
