# pylint: disable=no-name-in-module
from unittest.mock import MagicMock

import pytest
from scheduler import Scheduler

from cryptoward.utils.scheduler import JobScheduler


@pytest.fixture
def dummy_scheduler() -> MagicMock:
    return MagicMock(spec=Scheduler)


@pytest.fixture
def job_scheduler(dummy_scheduler: MagicMock) -> JobScheduler:
    scheduler = JobScheduler()
    scheduler.scheduler = dummy_scheduler
    return scheduler


@pytest.fixture
def job() -> MagicMock:
    return MagicMock()
