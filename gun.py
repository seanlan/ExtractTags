#coding:utf-8
'''
Created on 2016-4-19

@author: root
'''
import gevent.monkey
gevent.monkey.patch_all()
import multiprocessing


bind = "0.0.0.0:8090"
workers = multiprocessing.cpu_count() * 2 + 1

worker_class = 'gevent'
debug = True

worker_class = 'gunicorn.workers.ggevent.GeventWorker'

x_forwarded_for_header = 'X-FORWARDED-FOR'
