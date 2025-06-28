from cryptoward.injections import Environment, configure_injections
from cryptoward.scheduler import JobScheduler
from cryptoward.settings import Settings

from .job import job


def price_scrapper() -> None:
    job_scheduler = JobScheduler()
    job_scheduler.register_job(job, minutes=Settings.SCHEDULE_TIME_IN_MINUTES)
    job_scheduler.execute_jobs()


if __name__ == "__main__":
    configure_injections(Environment.PRODUCTION)
    price_scrapper()
