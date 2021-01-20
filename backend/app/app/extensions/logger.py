import os
import logging

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
            "fmt": '%(levelprefix)s %(asctime)s %(client_addr)s - "%(request_line)s" %(status_code)s',  # noqa: E501
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        "error": {
            "fmt": '%(levelprefix)s %(asctime)s %(client_addr)s - "%(request_line)s" %(status_code)s',  # noqa: E501
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    "handlers": {
        "default": {
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
            'filename': os.path.join(os.getcwd(), "..", "..", "..", "logs", "backend", "backend_info.log"),
            'when': 'MIDNIGHT',
            'backupCount': 0  # 保留日志备份数量  0默认不删除
        },
        "error": {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'error',
            'filename': os.path.join(os.getcwd(), "..", "..", "..", "logs", "backend", "backend_error.log"),
            'when': 'MIDNIGHT',
            'backupCount': 0  # 保留日志备份数量  0默认不删除
        },
    },
    "loggers": {
        "uvicorn": {"handlers": ["default"], "level": "INFO"},
        "uvicorn.error": {"level": "INFO"},
        "uvicorn.access": {"handlers": ["access"], "level": "INFO", "propagate": False},

        "backend": {"handlers": ["info", "error"], "level": "INFO"},
        "celery": {"handlers": ["info", "error"], "level": "INFO"},
    },
}

backend_logger = logging.getLogger("backend")

celery_logger = logging.getLogger("celery")
