set -e
#指明队列名称
nohup celery worker -A app.celery_app.worker.example -l info -Q example-queue -c 1 & > celery.log
