# -*- coding: utf-8*
from fabric.api import *
from notification import notice
import cuisine
import urllib


@task(default=True)
@runs_once
@notice
def init():
    execute(_init)


def _init():
    cuisine.select_package('apt')
    cuisine.select_hash('openssl')

    _setup_users()
    _setup_repositories()
    _setup_kataribe()


def _setup_kataribe():
    cuisine.package_ensure('wget')
    cuisine.package_ensure('unzip')

    if not cuisine.file_exists('/usr/local/bin/kataribe'):
        run('wget https://github.com/matsuu/kataribe/releases/download/v0.4.1/kataribe-v0.4.1_linux_amd64.zip')
        run('echo "34da63eb1696b964d30d9fac3b6c2778b9797eb4 kataribe-v0.4.1_linux_amd64.zip" | sha1sum -c -')
        run('unzip kataribe-v0.4.1_linux_amd64.zip kataribe')
        sudo('mv ./kataribe /usr/local/bin')
        run('rm kataribe-v0.4.1_linux_amd64.zip')


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

    if not cuisine.file_exists('/etc/apt/sources.list.d/percona-ps-80-release.list'):
        run('wget https://repo.percona.com/apt/percona-release_latest.$(lsb_release -sc)_all.deb')
        sudo('dpkg -i percona-release_latest.$(lsb_release -sc)_all.deb')
        run('rm percona-release_latest.$(lsb_release -sc)_all.deb')
        sudo('percona-release setup ps80')


def _setup_users():
    USERS = ['yuta1024', 'tyabuki', 'nhirokinet']
    for user in USERS:
        cuisine.user_ensure(user, shell='/bin/bash', passwd='yharima', encrypted_passwd=False)
        cuisine.group_user_ensure('sudo', user)
        # https://ubuntuforums.org/showthread.php?t=1318346
        cuisine.group_user_ensure('adm', user)
        with cuisine.mode_sudo():
            cuisine.ssh_authorize(user, _get_public_key_from_github(user))
    if not cuisine.is_ok(sudo('grep rsync /etc/sudoers && echo OK ; true')):
        sudo('echo "%s ALL=(ALL) NOPASSWD: /usr/bin/rsync" | EDITOR="tee -a" visudo' % ','.join(USERS))


def _get_public_key_from_github(user):
    url = 'https://github.com/%s.keys' % user
    return urllib.urlopen(url).read()
