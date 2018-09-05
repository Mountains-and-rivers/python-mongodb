
#!/usr/bin/env python
import os
import sys
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import time
try:
    import asyncio
except ImportError:
    import trollius as asyncio

now = lambda: time.time()
scheduler = AsyncIOScheduler()
def alarm(type):
    print ('[%s Alarm] This alarm was scheduled at %s.' % (type, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

# 定时执行
def corn_trigger():
    scheduler.add_job(func=alarm, args=['cron'], trigger='cron', second='*/5', id='corn_job')

async def do_some_work(x):
    print('Waiting: ', x)

    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)


start = now()

coroutine1 = corn_trigger()
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)


corn_trigger()


tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task ret: ', task.result())

print('TIME: ', now() - start)






