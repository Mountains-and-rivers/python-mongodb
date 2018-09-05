#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
import datetime
def check():
    sleep(5)
    time_stamp = datetime.datetime.now()
    print ("time_stamp       " + time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))
    print ("hello django-crontab")





