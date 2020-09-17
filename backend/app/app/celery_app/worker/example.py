# from raven import Client
"""
    启动脚本 - backend/app/celery_worker_start.sh
    #linux
    celery worker -A app.celery_app.worker.example -l info -Q main-queue -c 1
    #win
    celery worker -A app.celery_app.worker.example -l info -Q main-queue -c 1  -P eventlet

    CMD后台启动一个或多个职程
    celery multi start w1 -A {worker_name} -l info
"""
import os
from app.celery_app.celery_app import celery_app


# 用于SENTRY异常报告
# from app.core.config import settings
# client_sentry = Client(settings.SENTRY_DSN)


@celery_app.task(acks_late=True, )
def test_celery(word: str) -> str:
    import time
    time.sleep(3)
    return f"test task return {word}"


if __name__ == '__main__':
    celery_app.worker_main()

