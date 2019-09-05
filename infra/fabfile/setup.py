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

#     sudo('openssl dhparam -out /etc/nginx/dhparam.pem 2048')

    sudo('mkdir -p /var/248')
    sudo('chmod 777 /var/248')
    sudo('chmod -R 777 /var/log')

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
    sudo('debconf-set-selections <<< "percona-server-server percona-server-server/root-pass password Knishiya248!"')
    sudo('debconf-set-selections <<< "percona-server-server percona-server-server/re-root-pass password Knishiya248!"')
    # https://geert.vanderkelen.org/2018/mysql8-unattended-dpkg/
    sudo('debconf-set-selections <<< "percona-server-server percona-server-server/default-auth-override select Use Legacy Authentication Method (Retain MySQL 5.x Compatibility)"')
    sudo('apt install -y percona-server-server percona-toolkit')
    sudo('systemctl enable mysql')
    sudo('systemctl start mysql')
