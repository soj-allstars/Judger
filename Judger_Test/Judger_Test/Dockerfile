FROM python:3.8.0
WORKDIR /usr/src/judger
COPY . .
RUN bash setup.sh

CMD ["rq","worker","--url","redis://127.0.0.1:6379", "default", "check"]
