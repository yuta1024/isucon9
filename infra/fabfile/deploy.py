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
    sudo('mkdir -p /home/isucon/torb/webapp/php')

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

    rsync_project(
        local_dir='./etc/php/7.3/fpm/',
        remote_dir='/etc/php/7.3/fpm',
        extra_opts="--rsync-path='sudo rsync'"
    )

    rsync_project(
        local_dir='./etc/nginx/',
        remote_dir='/etc/nginx',
        extra_opts="--rsync-path='sudo rsync'"
    )

    # 頭の悪いなにか
    sudo('chmod -R 777 /var/log')

    # 先のsock生えてないとnginx起動できないのでこの順番で
    sudo('systemctl restart php7.3-fpm')
    sudo('systemctl restart nginx')


@task
@runs_once
@notice
def deploy_db():
    execute(_deploy_db)


def _deploy_db():
    rsync_project(
        local_dir='./etc/mysql/my.cnf',
        remote_dir='/etc/mysql/my.cnf',
        extra_opts="--rsync-path='sudo rsync'"
    )

    sudo('systemctl restart mysql')
