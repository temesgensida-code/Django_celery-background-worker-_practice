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
