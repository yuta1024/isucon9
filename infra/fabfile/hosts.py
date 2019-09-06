# -*- coding: utf-8*
from fabric.api import *

@task
def webapp():
    env.hosts = [
        '192.168.10.90',
        '192.168.10.92',
    ]

@task
def db():
    env.hosts = [
        '192.168.10.91'
    ]
