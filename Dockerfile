FROM jkswing/soj-judger-base:0.1
WORKDIR /usr/src/judger

COPY setup.sh requirements.txt ./
RUN bash setup.sh
COPY . .

ENTRYPOINT ["rq", "worker", "--url", "redis://soj-redis:6379"]
CMD ["default", "check"]
