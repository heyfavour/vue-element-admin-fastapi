set -e
#指明队列名称
celery worker -A app.celery_app.worker.example -2 info -Q example-queue -c 1
