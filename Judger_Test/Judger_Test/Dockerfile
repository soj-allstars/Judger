FROM python:3.8
WORKDIR /usr/src/judger
RUN apt-get update && apt-get install -y \
    pypy3 \
    default-jdk \
    sshfs && \
    rm -rf /var/lib/apt/lists/*

COPY setup.sh requirements.txt ./
RUN bash setup.sh
COPY . .
# TODO add USER
ENTRYPOINT ["rq", "worker", "--url", "redis://soj-redis:6379"]
CMD ["default", "check"]
