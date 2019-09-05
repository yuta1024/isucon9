# -*- coding: utf-8*
from fabric.api import *
from fabric.contrib.project import rsync_project
from notification import notice


@task
@runs_once
@notice
def deploy_webapp():
    execute(_deploy_webapp)


def _deploy_webapp():
    rsync_project(
        local_dir='../src/*',
        remote_dir='/home/isucon/torb/webapp/php',
        exclude=['db/', 'docker/', 'static', 'docker-compose.yaml', 'README.md'],
        extra_opts="--rsync-path='sudo rsync'"
    )

    rsync_project(
        local_dir='../src/static',
        remote_dir='/home/isucon/torb/webapp',
        extra_opts="--rsync-path='sudo rsync'"
    )

    rsync_project(
        local_dir='../src/db',
        remote_dir='/home/isucon/torb',
        extra_opts="--rsync-path='sudo rsync'"
    )

    # TODO: deploy config files for nginx and php

    sudo('systemctl restart nginx php7.3-fpm')


@task
@runs_once
@notice
def deploy_db():
    execute(_deploy_db)


def _deploy_db():
    # TODO: deploy config files for percona-server

    sudo('systemctl restart mysql')
