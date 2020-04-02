import os
import json

PROJECT_ROOT = '/usr/src/judger'

SOJ_HOST = os.environ.get('SOJ_HOST', '127.0.0.1')
RESULT_API_URL = f'http://{SOJ_HOST}/api/judge/result/'
SJ_RESULT_API_URL = f'http://{SOJ_HOST}/api/judge/solution-checker-result/'

LOG_DIR = f"{PROJECT_ROOT}/{os.environ.get('LOG_DIR', 'logs')}"
CHECKER_DIR = f"{PROJECT_ROOT}/{os.environ.get('CHECKER_DIR', 'checker_bin')}"

with open(f'{PROJECT_ROOT}/run_cfgs.json', 'r') as f:
    run_cfgs = json.load(f)
