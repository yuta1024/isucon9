# -*- coding: utf-8*
from fabric.api import *
import functools
import requests
import subprocess

# TODO: Revoke it after contests is ended
WEBHOOK_URL = 'https://discordapp.com/api/webhooks/618078607947989003/xT9A2caxLEuhFJHTNShloF-7ch6WXrwhBnqkGyLqFCHZFUbzkO2l560cXNBZFWBb4bKB'


def notice(func, here=False):
    @functools.wraps(func)
    def decorated(*args, **kwargs):
        func(*args, **kwargs)
        notify()
    return decorated


def notify():
    msg = [
        '`%s` executed `%s` the following servers(%s).' % (env.user, ', '.join(env.tasks), get_commit_hash()),
        '```',
        '\n'.join(map(lambda h: '- %s' % h, env.hosts)),
        '```'
    ]

    requests.post(
        WEBHOOK_URL,
        {
            'content': '\n'.join(msg)
        }
    )


def get_commit_hash():
    hash = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).strip()

    if subprocess.check_output(['git', 'status', '--porcelain']).strip() != '':
        return '`%s` + local changes' % hash
    return '`%s`' % hash
