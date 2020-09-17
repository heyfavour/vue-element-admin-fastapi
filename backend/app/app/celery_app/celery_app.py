from celery import Celery

# celery_app = Celery("worker", broker="amqp://guest@queue//")
celery_app = Celery(
    "worker",
    backend="redis://:wzx940516@49.235.242.224:6379/0",
    broker="redis://:wzx940516@49.235.242.224:6379/1",
)
# 处理队列 如果不定义会进入默认队列
celery_app.conf.task_routes = {"app.celery_app.worker.example.*": "example-queue"}
