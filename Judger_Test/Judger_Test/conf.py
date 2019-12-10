import os
from redis import Redis
from rq import Queue

SOJ_HOST = os.environ.get('SOJ_HOST', '47.106.140.231')
RESULT_API_URL = f'http://{SOJ_HOST}/api/judge/result/'

redis = Redis(os.environ.get('REDIS_HOST', '47.106.140.231'))
judge_q = Queue('judge', connection=redis)
result_q = Queue('result', connection=redis)
