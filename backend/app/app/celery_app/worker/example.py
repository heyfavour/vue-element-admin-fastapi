#from raven import Client
import os
import os
if os.name in ('posix'):os.sys.path.append(os.getcwd() + "/../../..")
else:os.sys.path.append(os.getcwd() + "\\..\\..\\..")
from app.celery_app.celery_app import celery_app


#用于SENTRY异常报告
#from app.core.config import settings
#client_sentry = Client(settings.SENTRY_DSN)


@celery_app.task(acks_late=True,)
def test_celery(word: str) -> str:
    return f"test task return {word}"

if __name__ == '__main__':
    celery_app.worker_main()
    #CMD多进程
    #celery -A {worker_name} worker --loglevel=info
    #CMD后台启动一个或多个职程
    #celery multi start w1 -A {worker_name} -l info
