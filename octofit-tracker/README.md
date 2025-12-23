# OctoFit Tracker (skeleton)

This folder contains a minimal skeleton for the OctoFit Tracker app.

Backend (Django):
- Location: `octofit-tracker/backend`
- Create a virtual environment: `python3 -m venv octofit-tracker/backend/venv`
- Activate and install: `source octofit-tracker/backend/venv/bin/activate` then `pip install -r octofit-tracker/backend/requirements.txt`
- Run migrations: `python octofit-tracker/backend/manage.py migrate`
- Start dev server: `python octofit-tracker/backend/manage.py runserver 8000`

Frontend (React + Vite):
- Location: `octofit-tracker/frontend`
- Install: `npm install`
- Dev server: `npm run dev` (default port from Vite)

Notes:
- The backend uses a small `tracker` app with an `Activity` model and a REST endpoint at `/api/activities/`.
- This is a starting point — let me know which features you'd like next (auth, profiles, leaderboards).
