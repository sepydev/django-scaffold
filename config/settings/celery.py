from __future__ import annotations

from typing import TYPE_CHECKING

from .base import TIME_ZONE
from .base import env

if TYPE_CHECKING:
    from typing import Any

CELERY_BROKER_URL = env("CELERY_BROKER_URL", default="redis://redis:6379/0")  # type: ignore[has-type]
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND", default="redis://redis:6379/0")  # type: ignore[has-type]
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = TIME_ZONE
CELERY_ENABLE_UTC = True
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_RESULT_EXPIRES = 3600
CELERY_TASK_ROUTES: dict[str, Any] = {
    # Example: Route specific tasks to specific queues
    # 'myapp.tasks.heavy_task': {'queue': 'heavy'},
    # 'myapp.tasks.light_task': {'queue': 'light'},
}
CELERY_WORKER_PREFETCH_MULTIPLIER = 1
CELERY_TASK_ACKS_LATE = True
