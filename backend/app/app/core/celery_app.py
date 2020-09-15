from celery import Celery

#celery_app = Celery("worker", broker="amqp://guest@queue//")
celery_app = Celery(
    "worker",
    backend="redis://:wzx940516@49.235.242.224:6379/0",
    broker="redis://:wzx940516@49.235.242.224:6379/1"
)

celery_app.conf.task_routes = {"app.worker.test_celery": "main-queue"}
