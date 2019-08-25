# -*- coding: utf-8*
from fabric.api import *
import cuisine
import urllib

USERS = ['yuta1024', 'tyabuki', 'nhirokinet']

cuisine.select_package('apt')
cuisine.select_hash('openssl')

@task
def init():
    _setup_users()
    _setup_repositories()


def _setup_repositories():
    _setup_nginx_repository()
    _setup_php73_repository()
    _setup_percona_repository()


def _setup_nginx_repository():
    # http://nginx.org/en/linux_packages.html#Ubuntu
    cuisine.package_ensure('curl')
    cuisine.package_ensure('gnupg2')
    cuisine.package_ensure('ca-certificates')
    cuisine.package_ensure('lsb-release')

    if not cuisine.file_exists('/etc/apt/sources.list.d/nginx.list'):
        sudo('echo "deb http://nginx.org/packages/mainline/ubuntu `lsb_release -cs` nginx" | sudo tee /etc/apt/sources.list.d/nginx.list')
        sudo('curl -fsSL https://nginx.org/keys/nginx_signing.key | apt-key add -')
        sudo('apt-key fingerprint ABF5BD827BD9BF62')


def _setup_php73_repository():
    # https://launchpad.net/~ondrej/+archive/ubuntu/php
    cuisine.package_ensure('software-properties-common')

    if not cuisine.file_exists('/etc/apt/sources.list.d/ondrej-ubuntu-php-bionic.list'):
        sudo('add-apt-repository ppa:ondrej/php -y')


def _setup_percona_repository():
    # https://www.percona.com/doc/percona-server/5.7/installation/apt_repo.html
    cuisine.package_ensure('wget')

    if not cuisine.file_exists('/etc/apt/sources.list.d/percona-original-release.list'):
        run('wget https://repo.percona.com/apt/percona-release_latest.$(lsb_release -sc)_all.deb')
        sudo('dpkg -i percona-release_latest.$(lsb_release -sc)_all.deb')
        run('rm percona-release_latest.$(lsb_release -sc)_all.deb')


def _setup_users():
    for user in USERS:
        cuisine.user_ensure(user, shell='/bin/bash', passwd='yharima', encrypted_passwd=False)
        cuisine.group_user_ensure('sudo', user)
        with cuisine.mode_sudo():
            cuisine.ssh_authorize(user, _get_public_key_from_github(user))


def _get_public_key_from_github(user):
    url = 'https://github.com/%s.keys' % user
    return urllib.urlopen(url).read()
