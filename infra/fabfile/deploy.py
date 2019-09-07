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
        local_dir='../src/php/src/*',
        remote_dir='/home/isucon/isucari/webapp/php/src',
        extra_opts="--rsync-path='sudo rsync'"
    )

    rsync_project(
        local_dir='../src/sql/*',
        remote_dir='/home/isucon/isucari/webapp/sql',
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
