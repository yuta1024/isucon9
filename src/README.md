# src
## About
PHP application files for ISUCON9.  
An application of ISUCON 7/8 worked and passed benchmark tests.

## Requirements
- Docker >= 19.03
- docker-compose >= 1.24

## Development with docker
#### 1. Mounts application files to `app` container
Adds lines to `volumes` in `app` of `docker-compose.yaml`.
- `/opt/isucon/webapp/php`
  - PHP application files
- `/opt/isucon/webapp/static`
  - Static files (e.g. CSS, favicon or JavaScript)

#### 2. Replaces `MYSQL_DATABASE` value
Replaces `<REPLACE_ME>` to ISUCON9 database name in `docker-compose.yaml`.

e.g. ISUCON8 database name is `torb`.

#### 3. Builds an application image
Executes a following command and builds an application image(includes nginx and php).  
**If `Dockerfile` modified, needs to rebuild.**
```
$ docker-compose build
```

#### 4. Launchs an application
Executes a following command and access to http://localhost:8080.
```
$ docker-compose up -d
```

## Appendix
#### Setup to schema or data for the first time
Mounts sql files to `/docker-entrypoint-initdb.d` in `db` container.

https://hub.docker.com/_/percona

#### Cleans up database
```
$ rm -r docker/mysql-data
```
