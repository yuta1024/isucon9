# -*- coding: utf-8*
from fabric.api import *
from notification import notice
import cuisine


@task
@runs_once
@notice
def install_nginx_and_php():
    execute(_install_nginx_and_php)


def _install_nginx_and_php():
    cuisine.select_package('apt')
    sudo('apt install -y nginx php7.3 php7.3-fpm php7.3-json php7.3-mbstring php7.3-mysql php7.3-opcache mysql-client')
    sudo('systemctl enable nginx php7.3-fpm')
    sudo('systemctl start nginx php7.3-fpm')


@task
@runs_once
@notice
def install_percona_server():
    execute(_install_percona_server)


def _install_percona_server():
    cuisine.select_package('apt')
    # https://jfg-mysql.blogspot.com/2018/11/howto-install-percona-server-57-on-debian-without-root-password-prompt.html
    sudo('debconf-set-selections <<< "percona-server-server-5.7 percona-server-server-5.7/root-pass password Knishiya248!"')
    sudo('debconf-set-selections <<< "percona-server-server-5.7 percona-server-server-5.7/re-root-pass password Knishiya248!"')
    sudo('apt install -y percona-server-server-5.7 percona-toolkit')
    sudo('systemctl enable mysql')
    sudo('systemctl start mysql')
