FROM php:7.2-fpm

#
# Benötigte Pakete installieren
#
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y -o Dpkg::Options::="--force-confold" --no-install-recommends --no-install-suggests \
    curl \
    git \
    gnupg \
    graphicsmagick \
    imagemagick \
    locales \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libncurses5-dev \
    libicu-dev \
    libmemcached-dev \
    libcurl4-openssl-dev \
    libpng-dev \
    libgmp-dev \
    libxml2-dev \
    libldap2-dev \
    libffi-dev \
    libzip-dev \
    mariadb-client \
    python-pip \
    python3-pip \
    python3 \
    python-dev \
    ruby \
    ruby-dev \
    rsync \
    sshpass \
    msmtp \
    vim \
    zlib1g-dev \
    netcat \
    ssh \
    iputils-ping \
    python3-setuptools \
    python-cffi \
 && rm -rf /var/lib/apt/lists/*

#
#
#
RUN docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \
 && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
 && docker-php-ext-install -j$(nproc) \
    exif \
    gd \
    intl \
    mysqli \
    pdo_mysql \
    zip

#
#
#
RUN pip3 install -U pip
RUN pip3 install paramiko
RUN pip3 install future-fstrings

#
# https://forums.docker.com/t/ssh-from-one-containe-to-another-container/65906/9
#
RUN mkdir /var/run/sshd && \
    chmod 0755 /var/run/sshd && \
    useradd -p $(openssl passwd -1 password) --create-home --shell /bin/bash --groups sudo user

RUN mkdir /root/.ssh && \
    ssh-keyscan -H www1 >> ~/.ssh/known_hosts && \
    ssh-keyscan -H www2 >> ~/.ssh/known_hosts

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]