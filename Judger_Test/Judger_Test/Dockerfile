FROM python:3.8
WORKDIR /usr/src/judger
COPY . .
RUN bash setup.sh

ENTRYPOINT ["rq", "worker", "--url", "redis://soj-redis:6379"]
CMD ["default", "check"]
