FROM python:3.8.0
WORKDIR /usr/src/judger
COPY . .
RUN bash setup.sh

CMD ["rq","worker","--url","redis://47.106.140.231:6379"]
