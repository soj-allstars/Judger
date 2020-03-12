import os
from redis import Redis
from rq import Queue

SOJ_HOST = os.environ.get('SOJ_HOST', '127.0.0.1')
RESULT_API_URL = f'http://{SOJ_HOST}/api/judge/result/'
SJ_RESULT_API_URL = f'http://{SOJ_HOST}/api/judge/solution-checker-result/'

redis = Redis(os.environ.get('REDIS_HOST', '127.0.0.1'))
judge_q = Queue('judge', connection=redis)
result_q = Queue('result', connection=redis)

LOG_DIR = os.environ.get('LOG_DIR', 'logs')
CHECKER_DIR = os.environ.get('CHECKER_DIR', 'testlib/bin')
