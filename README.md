# Django Authentication System

A full authentication system built with Django, implementing registration, login, logout, session management, and protected pages — using a custom user model and custom authentication backend.

---

## Features

- **Custom User Model** — extends `AbstractUser` with unique, case-insensitive email enforcement
- **Profile Model** — linked via `OneToOneField`, stores phone number separately
- **Registration** — with duplicate username/email detection and password confirmation validation
- **Login** — supports both email and username via a custom authentication backend
- **Session Management** — Django session-based auth with session ID stored in browser cookie, data in database
- **Protected Pages** — `@login_required` with `?next=` redirect handling
- **Logout** — full session flush on logout
- **Flash Messages** — success and error feedback throughout

---

## Tech Stack

- Python 3.x
- Django 5.x
- SQLite (default development database)

---

## Project Structure

```
auth_project/
├── auth_project/
│   ├── settings.py
│   └── urls.py
├── auth_app/
│   ├── backends.py       # Custom authentication backend
│   ├── forms.py          # SignUpForm with validation
│   ├── models.py         # CustomUser and Profile models
│   ├── views.py          # All views
│   ├── urls.py           # App-level URL routing
│   ├── admin.py          # Model registration
│   └── templates/
│       └── auth_app/
│           ├── base.html
│           ├── signup.html
│           ├── login.html
│           └── dashboard.html
└── manage.py
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/auth_project.git
cd auth_project
```

### 2. Create and activate a virtual environment

```bash
python -m venv authenv
# Windows
authenv\Scripts\activate
# Mac/Linux
source authenv/bin/activate
```

### 3. Install dependencies

```bash
pip install django
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (to access admin panel)

```bash
python manage.py createsuperuser
```

### 6. Run the server

```bash
python manage.py runserver
```

### 7. Visit the app

| Page | URL |
|---|---|
| Home | http://127.0.0.1:8000/auth_app/ |
| Register | http://127.0.0.1:8000/auth_app/register/ |
| Login | http://127.0.0.1:8000/auth_app/login/ |
| Dashboard (protected) | http://127.0.0.1:8000/auth_app/dashboard/ |
| Admin | http://127.0.0.1:8000/admin/ |

---

## Key Technical Decisions

**Custom User Model**
Extended `AbstractUser` instead of building from scratch to keep all default Django user functionality while adding `unique=True` on the email field. Referenced via `settings.AUTH_USER_MODEL` throughout to avoid circular imports.

**Custom Authentication Backend**
Django's default backend only supports username login. A custom backend in `backends.py` uses a `Q` query with `iexact` lookups to support login with either email or username, case-insensitively.

**Form-Level Duplicate Detection**
Duplicate username and email are caught in `clean_username()` and `clean_email()` before hitting the database. An `IntegrityError` catch in the view acts as a safety net for race conditions.

**Session-Based Authentication**
Uses Django's built-in session framework. Session ID stored as a browser cookie; session data stored in the `django_session` database table. Logout flushes all session data and cycles the session key.

---

## Environment Variables

For production, move the following out of `settings.py` into environment variables:

```
SECRET_KEY
DEBUG
DATABASE_URL
```
