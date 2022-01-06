from apscheduler.schedulers.background import BackgroundScheduler
from myapp.utilities import clearall
from turfs.utilities import changeday
from turfs.models import Turfs

sched = BackgroundScheduler()

@sched.scheduled_job('cron', hour=23, minute=59)
def job1():
    clearall()
    changeday()
sched.start()