# OctoFit Tracker

This repository contains the OctoFit Tracker app scaffold.

## Structure

- `octofit-tracker/backend/` - Django backend and API
- `octofit-tracker/frontend/` - frontend application

## Backend setup

1. Create a Python virtual environment:

   ```bash
   python3 -m venv octofit-tracker/backend/venv
   ```

2. Activate the virtual environment:

   ```bash
   source octofit-tracker/backend/venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r octofit-tracker/backend/requirements.txt
   ```

## Notes

- Use Django ORM for database models.
- The backend will target MongoDB via `djongo`.
