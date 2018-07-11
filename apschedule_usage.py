from apscheduler.schedulers.blocking import BlockingScheduler
import time
import datetime
sched = BlockingScheduler()
 
@sched.scheduled_job('interval', seconds=10)
def timed_job():
    print('This job is run every three minutes.')
    print(time.ctime())

@sched.scheduled_job('cron', day_of_week='mon-fri', hour='16-19', minute='30-59', second='*/3')
def scheduled_job():
	print('This job is run every 3 mins')


print('before the start funciton')
sched.start()
print("let us figure out the situation")



