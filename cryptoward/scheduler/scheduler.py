import datetime as dt
import time
from dataclasses import dataclass
from typing import Any, Callable

from scheduler import Scheduler


@dataclass
class JobScheduler:
    _scheduler: Scheduler | None = None

    @property
    def scheduler(self) -> Scheduler:
        if self._scheduler is None:
            self._scheduler = Scheduler()
        return self._scheduler

    def register_job(self, job: Callable[..., Any], minutes: int) -> None:
        self.scheduler.cyclic(dt.timedelta(minutes=minutes), job)

    def execute_jobs(self) -> None:
        while True:
            self.scheduler.exec_jobs()
            time.sleep(1)
