from power_api.core.settings import settings

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DEFAULT_HANDLERS = [
    "console",
    "file",
]

LOGGING = {  # noqa
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {"format": LOG_FORMAT},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file": {
            "level": "DEBUG",
            "formatter": "verbose",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": f"{settings().logs.path}/api.log",
            "backupCount": 5,
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
        },
    },
    "root": {
        "level": "INFO",
        "formatter": "verbose",
        "handlers": LOG_DEFAULT_HANDLERS,
    },
}
