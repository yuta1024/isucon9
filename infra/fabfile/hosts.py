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
        '47.74.2.106'
    ]
