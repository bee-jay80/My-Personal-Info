# Me — Personal Info (Django)

A small Django app that displays personal information after a simple password gate. The frontend focuses on a dark/blue/white theme with subtle animations and a loading overlay.

## Features
- Password-gated single-user dashboard (password held in environment variable)
- CSS animations and a loading overlay when submitting the password
- Simple HTML templates: `main.html`, `login.html`, `dashboard.html`

## Requirements
- Python 3.11+ (3.13 is shown in the project environment)
- pip
- virtualenv (recommended)

## Setup (local development)

1. Create and activate a virtual environment

```bash
python -m venv venv
# On Windows (bash):
source venv/Scripts/activate
# On Unix/macOS:
# source venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root (example values)

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
BVN=***********
NIN=***********
EMAIL=you@example.com
PHONE=**********
PASSWORD=MySecretPassword
```

4. Run migrations and collect static (for production-like static serving)

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

5. Run the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` and enter the password from the `.env` to access the dashboard.

## Notes
- The current password check compares the POSTed password to the `PASSWORD` environment variable. This is a simple, single-user gating mechanism. For multi-user support use Django's authentication system.
- During development you can set `DEBUG=True` in `.env` so Django's staticfiles will be served automatically. In production, set `DEBUG=False` and use WhiteNoise or a web server to serve static files (the project already includes WhiteNoise middleware).
- The project uses environment variables for sensitive values; keep `.env` out of version control (the provided `.gitignore` excludes common secrets and virtual environments).