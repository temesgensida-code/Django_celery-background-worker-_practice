# Django + Celery + React (Linux Setup)

This project was originally created in a Windows workflow. These steps run it cleanly on Linux.

## 1) Backend setup (Django + Celery)

```bash
cd Django_celery-background-worker-_practice
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
```

## 2) Run backend processes

Open 3 terminals in the project root with the same virtualenv activated:

Terminal A:
```bash
python manage.py runserver
```

Terminal B:
```bash
celery -A myapp worker -l info
```

Terminal C:
```bash
celery -A myapp beat -l info
```

Notes:
- By default, Celery uses a local filesystem broker under `control/`.
- Beat schedule is database-backed via `django_celery_beat` (cloud-friendly, no local `celerybeat-schedule` file required).
- The periodic task `update-joke-every-2-seconds` is created by migration and can be edited in Django admin.
- You can switch to Redis by setting `CELERY_BROKER_URL`, for example:
  `export CELERY_BROKER_URL=redis://127.0.0.1:6379/0`

## 3) Frontend setup (React + Vite)

```bash
cd displayer
npm install
npm run dev
```

## 4) API endpoints

- `GET /api/joke/`
- `GET /api/joke/stream/`

## 5) Exact Commands Used (Linux)

Run once after clone:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate --noinput
cd displayer
npm install
cd ..
```

Run the full stack (4 terminals):

Terminal 1 (Django):
```bash
cd /home/temesgensida/tom/django_react/celery/Django_celery-background-worker-_practice
source .venv/bin/activate
python manage.py runserver
```

Terminal 2 (Celery worker):
```bash
cd /home/temesgensida/tom/django_react/celery/Django_celery-background-worker-_practice
source .venv/bin/activate
celery -A myapp worker -l info
```

Terminal 3 (Celery beat):
```bash
cd /home/temesgensida/tom/django_react/celery/Django_celery-background-worker-_practice
source .venv/bin/activate
celery -A myapp beat -l info
```

Terminal 4 (React dev server):
```bash
cd /home/temesgensida/tom/django_react/celery/Django_celery-background-worker-_practice/displayer
npm run dev -- --host
```

Quick health checks:

```bash
curl -s http://127.0.0.1:8000/api/joke/
curl -N http://127.0.0.1:8000/api/joke/stream/
```

## 6) Azure deployment quick start

This repo is cloud-ready with environment-driven Django config and database-backed beat schedule.

1. Configure App Settings using [.env.azure.example](.env.azure.example).
2. Use startup commands from [deploy/azure-start-commands.txt](deploy/azure-start-commands.txt).
3. Follow the full guide in [deploy/AZURE_DEPLOYMENT.md](deploy/AZURE_DEPLOYMENT.md).
4. For VS Code Azure extension workflow, use [deploy/AZURE_VSCODE_EXTENSION_STEPS.md](deploy/AZURE_VSCODE_EXTENSION_STEPS.md).

Recommended Azure services:

- App Service Linux for `web`, `worker`, and `beat`
- Azure Database for PostgreSQL (shared `DATABASE_URL`)
- Azure Cache for Redis (shared `CELERY_BROKER_URL`)
