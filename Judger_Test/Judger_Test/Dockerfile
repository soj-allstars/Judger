FROM python:3.8.0
WORKDIR /usr/src/judger
COPY testjson.json answer.txt job_dealer.py conf.py  ./
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip && \
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir rq &&\
	pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir requests

CMD ["rq","worker","--url","redis://47.106.140.231:6379"]

