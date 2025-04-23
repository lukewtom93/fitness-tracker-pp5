# Fitness Tracker

A full-stack web application that allows users to log workouts, track progress, and stay motivated on their fitness journey.

## Features

- **User Authentication** – Sign up, log in, and manage your account securely.
- **Workout Logging** – Add, update, and delete workouts.
- **Progress Tracking** – View your workout history in a user-friendly dashboard.
- **Responsive Design** – Works seamlessly across desktop and mobile devices.

## Built With

**Frontend:**
- React.js
- HTML 
- CSS
- Bootstrap

**Backend:**
- Django
- Django REST Framework

**Database:**
- PostgreSQL

**Deployment:**
- Heroku

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/lukewtom93/fitness-tracker-pp5.git
cd fitness-tracker-pp5
```

### 2. Backend Setup (Django)

```bash
cd backend
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 3.Frontend Setup (React)

```bash
cd frontend
npm install
npm start
```
