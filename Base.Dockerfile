FROM python:3.8

RUN apt-get update && apt-get install -y \
    pypy3 \
    default-jdk \
    sshfs && \
    rm -rf /var/lib/apt/lists/*
