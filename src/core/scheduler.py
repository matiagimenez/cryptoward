import schedule
import time


class Scheduler:
    @classmethod
    def schedule_job(cls, job) -> None:
        # schedule.every(12).hours.do(job)
        schedule.every(5).seconds.do(job)
        # schedule.every(1).minute.do(job)
        while True:
            schedule.run_pending()
            time.sleep(1)
