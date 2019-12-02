FROM python:3.8.0
WORKDIR /usr/src/judger
COPY Judger_Test.py testjson.json answer.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir rq &&\
	pip install --no-cache-dir requests

CMD ["python","Judger_Test.py"]

