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


def _setup_users():
    for user in USERS:
        cuisine.user_ensure(user, shell='/bin/bash', passwd='yharima', encrypted_passwd=False)
        cuisine.group_user_ensure('sudo', user)
        with cuisine.mode_sudo():
            cuisine.ssh_authorize(user, _get_public_key_from_github(user))


def _get_public_key_from_github(user):
    url = 'https://github.com/%s.keys' % user
    return urllib.urlopen(url).read()
