#!/usr/bin/env python
import os
import sys
from threading import Thread
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import time
from time import sleep
def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target = f, args = args, kwargs = kwargs)
        thr.start()
    return wrapper


try:
    import asyncio
except ImportError:
    import trollius as asyncio

scheduler = AsyncIOScheduler()

def alarm(type):
    print ('[%s Alarm] This alarm was scheduled at %s.' % (type, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


# 定时执行
def corn_trigger():
    scheduler.add_job(func=alarm, args=['cron'], trigger='cron', second='*/5', id='corn_job')

# Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.


def timer_work():
    scheduler.add_job(func=alarm, args=['cron'], trigger='cron', second='*/5', id='corn_job')
    scheduler.start()

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_blog.settings")
    from django.core.management import execute_from_command_line

    # scheduler.add_job(func=alarm, args=['cron'], trigger='cron', second='*/5', id='corn_job')
    execute_from_command_line(sys.argv)
    # 创建两个线程
    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    # try:
    #     asyncio.get_event_loop().run_forever()
    # except (KeyboardInterrupt, SystemExit):
    #     pass

