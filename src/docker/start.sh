#!/bin/sh

set -eu

/usr/sbin/php-fpm7.3
/usr/sbin/nginx -g "daemon off;"
