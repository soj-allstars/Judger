FROM python:3.8

RUN wget https://bitbucket.org/pypy/pypy/downloads/pypy3.6-v7.3.1-linux64.tar.bz2 && \
    tar xf pypy3.6-v7.3.1-linux64.tar.bz2 && \
    ln -s /pypy3.6-v7.3.1-linux64/bin/pypy3 /usr/local/bin/pypy3 && \
    apt-get update && apt-get install -y \
        default-jdk && \
    rm pypy3.6-v7.3.1-linux64.tar.bz2 && \
    rm -rf /var/lib/apt/lists/*
