set -e

celery worker -A app.celery_app.worker.example -l info -Q main-queue -c 1
