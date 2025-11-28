import datetime as dt
from unittest.mock import MagicMock, patch

import pytest

from cryptoward.utils import Settings
from cryptoward.utils.scheduler import JobScheduler


def test_initialization() -> None:
    job_scheduler = JobScheduler()
    assert job_scheduler.scheduler is not None


def test_register_job(job_scheduler: JobScheduler, job: MagicMock) -> None:
    job_scheduler.register_job(job, Settings.SCHEDULE_TIME_IN_MINUTES)

    job_scheduler.scheduler.cyclic.assert_called_once_with(
        dt.timedelta(minutes=Settings.SCHEDULE_TIME_IN_MINUTES), job
    )


def test_execute_jobs(job_scheduler: JobScheduler, dummy_scheduler: MagicMock) -> None:
    # Patch time.sleep to raise an exception to break the infinite loop
    with (
        patch("cryptoward.utils.scheduler.time.sleep", side_effect=InterruptedError),
        pytest.raises(InterruptedError),
    ):
        job_scheduler.execute_jobs()

    dummy_scheduler.exec_jobs.assert_called_once()
