from cryptoward.helpers import fetch_cryptocurrency_prices
from cryptoward.injections import Environment, configure_injections
from cryptoward.utils import JobScheduler, Level, Settings, log


def main() -> None:
    log("Application started", Level.INFO)
    job_scheduler = JobScheduler()
    job_scheduler.register_job(
        fetch_cryptocurrency_prices,
        minutes=Settings.SCHEDULE_TIME_IN_MINUTES,
    )
    job_scheduler.execute_jobs()


if __name__ == "__main__":
    configure_injections(Environment.PRODUCTION)
    main()
