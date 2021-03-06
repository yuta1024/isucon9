# infra
## About
Deployment scirpts for [ISUCON9](http://isucon.net/archives/53231706.html).

## Requirements
- Python >= 2.7, < 3

## Setup
```
$ pip install 'fabric<2' cuisine requests
```

## Tasks
### init
Initializes servers. **Default sudo password is `yharima`.**

#### _setup_users
Creates following users using public keys of GitHub.
- [yuta1024](https://github.com/yuta1024)
- [tyabuki](https://github.com/tyabuki)
- [nhirokinet](https://github.com/nhirokinet)

#### _setup_repositories
Setup repositories of Nginx, PHP and Percona Server.
- Nginx(mainline): http://nginx.org/en/linux_packages.html#Ubuntu
- PHP: https://launchpad.net/~ondrej/+archive/ubuntu/php
- Percona Server: https://www.percona.com/doc/percona-server/5.7/installation/apt_repo.html

#### _setup_kataribe
Installs [kataribe](https://github.com/matsuu/kataribe) to `/usr/local/bin`.

### setup.install_nginx_and_php
Installs nginx and php.

### setup.install_percona_server
Installs percona-server. **Default MySQL root password is `Knishiya248!`.**  
`knishiya` is a member of `そり`. He is a super engineer so we are respecting him!

### deploy.deploy_webapp
Deploys files and config files of a web application and restart `nginx` and `php-fpm`.

### deploy.deploy_db
Deploys config files of a database and restart `mysql`.

### log.logrotate
Compresses logs and create new empty log files.

### log.kataribe
Collects access logs and analyzes them using kataribe.
