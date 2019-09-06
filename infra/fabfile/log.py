# -*- coding: utf-8*
from fabric.api import *
from notification import notice
import cuisine


@task
@runs_once
@notice
def logrotate():
    execute(_logrotate)


def _logrotate():
    date = run('date "+%y%m%d-%H%M%S"')
    if cuisine.file_exists('/var/log/nginx/access.log'):
        sudo('gzip -c /var/log/nginx/access.log > /var/log/nginx/access-%s.gz' % date)
        sudo(': > /var/log/nginx/access.log')
    if cuisine.file_exists('/var/log/nginx/error.log'):
        sudo('gzip -c /var/log/nginx/access.log > /var/log/nginx/error-%s.gz' % date)
        sudo(': > /var/log/nginx/error.log')


@task
@runs_once
def kataribe():
    execute(_kataribe)
    local('cat %s > merged.log' % ' '.join(env.hosts))
    local('rm %s' % ' '.join(env.hosts))
    local('cat merged.log | kataribe')


def _kataribe():
    if cuisine.file_exists('/var/log/nginx/access.log'):
        get('/var/log/nginx/access.log', env.host)
