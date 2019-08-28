FROM ubuntu:bionic

RUN set -x && \
    addgroup --system --gid 248 isucon && \
    adduser --system --disabled-login --ingroup isucon --no-create-home --home /nonexistent --shell /bin/false --uid 248 isucon && \
    apt update && \
    apt upgrade -y && \
    apt install -y curl gnupg2 ca-certificates lsb-release software-properties-common && \
    echo "deb http://nginx.org/packages/mainline/ubuntu `lsb_release -cs` nginx" | tee /etc/apt/sources.list.d/nginx.list && \
    curl -fsSL https://nginx.org/keys/nginx_signing.key | apt-key add - && \
    apt-key fingerprint ABF5BD827BD9BF62 && \
    add-apt-repository ppa:ondrej/php -y && \
    apt install -y nginx php7.3 php7.3-fpm php7.3-json php7.3-mbstring php7.3-mysql php7.3-opcache mysql-client && \
    apt autoremove -y && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /run/php/ && \
    mkdir /opt/isucon && \
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log && \
    sed -i -e 's/128M$/-1/' /etc/php/7.3/fpm/php.ini && \
    sed -i -e 's/2M$/128M/' /etc/php/7.3/fpm/php.ini

WORKDIR /opt/isucon
COPY start.sh start.sh
EXPOSE 80

CMD ["sh", "start.sh"]
