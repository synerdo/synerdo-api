from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "base": {
            "format": "{levelname} {asctime:s} {name} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            #"level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "base",
            "filters": ["require_debug_true"],
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "formatter": "base",
            "filename": BASE_DIR / "django.log"
        },
    },
    "loggers": {
        "django": {
            "level": "INFO",
            "handlers": ["console", "file"],
            "propagate": False,
        },
    }
}
