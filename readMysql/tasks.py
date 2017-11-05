# -*- coding: utf-8 -*-
'''
Created on 2017年11月4日
@author: hylc
'''
from celery import task
from readRedis import rRedis

    
@task
def add(x, y):
    while True:
        rRedis.add(rRedis)
    return x + y