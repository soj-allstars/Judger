FROM python
WORKDIR /usr/src/judger
COPY Judger_Test.py testjson.json answer.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir rq

CMD ["python","Judger_Test.py"]

