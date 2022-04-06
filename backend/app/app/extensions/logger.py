import os
import logging

from app.extensions.request_id import RequestIDLogFilter

class ErrorlevelFilter(logging.Filter):
    def filter(self, record):
        if record.levelno > logging.INFO:
            return False
        return True


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(asctime)s %(message)s",
            'datefmt': '%Y-%m-%d %H:%M:%S',
            "use_colors": None,
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '%(levelprefix)s %(asctime)s %(client_addr)s - "%(request_line)s" %(status_code)s',  # noqa: E501
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        "info": {
            "format": '%(levelname)s %(asctime)s %(request_id)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        "error": {
            "format": '%(levelname)s %(asctime)s %(request_id)s "%(filename)s" "%(funcName)s" "%(lineno)s" %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'filters': {
        'info_filter': {
            '()': ErrorlevelFilter,  # 使用 `()` 指定用哪个类来实现过滤功能
            'name': 'info_filter'  # name 的值会在 Filter 实例化时传入
        },
        'id_filter': {
            '()': RequestIDLogFilter,  # 使用 `()` 指定用哪个类来实现过滤功能
            'name': 'id_filter'  # name 的值会在 Filter 实例化时传入
        }
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "uvicorn_error": {
            'level': 'ERROR',
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "info": {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'info',
            'filters': ['info_filter',"id_filter"],
            'filename': os.path.join(os.path.dirname(__file__),"..","..", "..", "..", "logs", "backend", "backend_info.log"),
            'when': 'MIDNIGHT',
            'backupCount': 0  # 保留日志备份数量  0默认不删除
        },
        "error": {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'error',
            'filters': ["id_filter"],
            'filename': os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "logs", "backend","backend_error.log"),
            'when': 'MIDNIGHT',
            'backupCount': 0  # 保留日志备份数量  0默认不删除
        },
    },
    "loggers": {
        "uvicorn": {"handlers": ["default"], "level": "INFO"},
        "uvicorn.error": {"handlers": ["uvicorn_error","error"],"level": "INFO"},
        "uvicorn.access": {"handlers": ["access"], "level": "INFO", "propagate": False},

        "backend": {"handlers": ["info", "error"], "level": "INFO"},
        "celery": {"handlers": ["info", "error"], "level": "INFO"},
    },
}

backend_logger = logging.getLogger("backend")

celery_logger = logging.getLogger("celery")
