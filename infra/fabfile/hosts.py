# -*- coding: utf-8*
from fabric.api import *

@task
def webapp():
    env.hosts = [
        '47.91.22.47'
    ]

@task
def db():
    env.hosts = [
        '192.168.10.91'
    ]
