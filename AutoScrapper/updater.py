
from .newsScrapped import schedule_api
from apscheduler.schedulers.background import BackgroundScheduler

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule_api, 'interval', seconds=900)
    scheduler.start()