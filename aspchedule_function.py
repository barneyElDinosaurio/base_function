
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
 
import datetime
import time
# import logging
 
def job_function():
    print("Hello World" + " " + str(datetime.datetime.now()))
 
if __name__ == '__main__':
    # log = logging.getLogger('apscheduler.executors.default')
    # log.setLevel(logging.INFO)  # DEBUG
 
    # fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
    # h = logging.StreamHandler()
    # h.setFormatter(fmt)
    # log.addHandler(h)
 
    print('start to do it')
 
    sched = BlockingScheduler()
 
    # Schedules job_function to be run on the third Friday
    #  of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
    sched.add_job(job_function, 'cron', day_of_week='mon-fri', hour='16-19', minute="*", second="*/10")
    sched.start()
