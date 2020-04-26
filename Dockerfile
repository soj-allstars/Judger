FROM jkswing/soj-judger-base:0.2
WORKDIR /usr/src/judger

COPY setup.sh requirements.txt ./
RUN bash setup.sh
COPY . .

ENTRYPOINT ["rq", "worker", "-c", "rq_settings"]
CMD ["default", "check"]
