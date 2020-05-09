import os
import json

PROJECT_ROOT = '/usr/src/judger'

SOJ_HOST = os.environ.get('SOJ_HOST', '172.17.0.1')
RESULT_API_URL = f'http://{SOJ_HOST}/api/judge/result/'
SJ_RESULT_API_URL = f'http://{SOJ_HOST}/api/judge/solution-checker-result/'

LOG_DIR = f"{PROJECT_ROOT}/{os.environ.get('LOG_DIR', 'logs')}"
CHECKER_DIR = f"{PROJECT_ROOT}/{os.environ.get('CHECKER_DIR', 'checker_bin')}"
SUBMISSION_DIR = f"{PROJECT_ROOT}/{os.environ.get('SUBMISSION_DIR', 'submissions')}"

SUBMISSION_EXPIRE_HOURS = int(os.environ.get('SUBMISSION_EXPIRE_HOURS', 10))

with open(f'{PROJECT_ROOT}/run_cfgs.json', 'r') as f:
    run_cfgs = json.load(f)
