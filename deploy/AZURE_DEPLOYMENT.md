# Azure Deployment Guide (Django + Celery + React)

This repo is now configured to deploy to Azure with environment-based settings.

## Recommended architecture

- Azure App Service (Linux) for Django web app
- Azure App Service (Linux) for Celery worker
- Azure App Service (Linux) for Celery beat
- Azure Database for PostgreSQL for shared Django data
- Azure Cache for Redis for Celery broker
- Optional: host React frontend on Azure Static Web Apps

## 1) Prepare environment settings

Copy values from `.env.azure.example` into Azure App Settings for each app.

Minimum required for cloud:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=False`
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_CSRF_TRUSTED_ORIGINS`
- `DATABASE_URL` (PostgreSQL)
- `CELERY_BROKER_URL` (Redis)

## 2) Startup commands per app

Use commands from `deploy/azure-start-commands.txt`.

- Web app startup command: run migrations + collectstatic + gunicorn
- Worker app startup command: celery worker
- Beat app startup command: celery beat

## 3) Deployment flow

1. Create/provision three App Service apps (web, worker, beat) on Linux.
2. Deploy the same repo code to all three apps.
3. Set app settings on all apps (same `DATABASE_URL` and `CELERY_BROKER_URL`).
4. Assign startup command per app from `deploy/azure-start-commands.txt`.
5. Restart apps and verify logs.

## 4) Notes

- Beat schedule is database-backed (`django_celery_beat`), so no local beat schedule file is required.
- SQLite and filesystem broker are for local dev only.
- In Azure, always use PostgreSQL + Redis shared by all three processes.
