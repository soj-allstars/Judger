import os
import conf
import requests
import logging
from consts import VerdictResult, RESULT_STR
from exceptions import ExecutorInitException
from executors import get_executor
from checkers import get_checker
import json
from checkers.special_judger import SpecialJudgeSpawner


def check_solution_and_checker(**detail):
    solution_code = detail['solution_code']
    solution_lang = detail['solution_lang']
    problem_id = detail['problem_id']
    time_limit = detail['time_limit']
    memory_limit = detail['memory_limit']
    channel_name = detail['channel_name']

    problem_dir = f'problems/{problem_id}'

    result = {
        'solution': {},
        'special_judge': {},
    }

    try:
        try:
            solution_executor = get_executor(solution_lang, solution_code, f'{problem_dir}/solution')
            result['solution'] = get_solution_answers(problem_dir, solution_executor, time_limit, memory_limit)
        except ExecutorInitException as e:
            result['solution']['verdict'] = VerdictResult.CE
            result['solution']['desc'] = str(e)

        sj_code = detail.get('sj_code')
        sj_name = detail.get('sj_name')
        if sj_code is not None:
            log_file_path = f'{conf.LOG_DIR}/sj_{sj_name}.log'

            sj_spawner = SpecialJudgeSpawner(sj_code, None, sj_name)

            result['special_judge'] = sj_spawner.execute(None, None, log_file_path, 5000, 256 * 1024)  # compile here
    finally:
        result = {'problem_id': problem_id, 'channel_name': channel_name, 'result': json.dumps(result)}
        send_result_back(conf.SJ_RESULT_API_URL, result)


def get_solution_answers(problem_dir, solution_executor, time_limit, memory_limit):
    result = {
        "verdict": VerdictResult.AC,
        "desc": "",
        "time_usage": 0,
        "memory_usage": 0,
        "outputs": [],
    }

    case_no = 1
    while True:
        input_path = f'{problem_dir}/{case_no}.in'
        answer_path = f'{problem_dir}/{case_no}.ans'
        log_path = f'{problem_dir}/{case_no}.log'
        # processed all test cases
        if not os.path.isfile(input_path):
            break

        solution_res = solution_executor.execute(input_path, answer_path, log_path, time_limit, memory_limit, trace=True)
        if solution_res['result'] != VerdictResult.AC:
            result['verdict'] = VerdictResult.CE
            result['desc'] = (f'Solution has verdict <{RESULT_STR[solution_res["result"]]}> instead of <{RESULT_STR[VerdictResult.AC]}>\n'
                              f'{solution_res.get("desc", "")}')
            return result

        result['time_usage'] = max(result['time_usage'], solution_res['timeused'])
        result['memory_usage'] = max(result['memory_usage'], solution_res['memoryused'])
        with open(answer_path, 'r') as f:
            result['outputs'].append(f.read())

        if solution_res['result'] != VerdictResult.AC:
            result['verdict'] = solution_res['result']
            result['desc'] = solution_res.get('desc', '')
            return result

        case_no += 1

    return result


def judge_submission(**submit_detail):
    submitted_code = submit_detail["submitted_code"]
    submitted_lang = submit_detail['submitted_lang']
    submit_id = submit_detail['submit_id']

    result = {
        "verdict": VerdictResult.SE,
        "desc": "",
        "time_usage": 0,
        "memory_usage": 0,
        "outputs": [],
    }

    try:
        submission_dir = f'submissions/{submit_id}'
        try:
            submitted_executor = get_executor(submitted_lang, submitted_code, f'{submission_dir}/submitted')
        except ExecutorInitException as e:
            result['verdict'] = VerdictResult.CE
            result['desc'] = str(e)
            return result
        result = do_judge(submit_detail, submission_dir, submitted_executor)
    finally:
        result = {'submit_id': submit_id, 'result': json.dumps(result)}
        send_result_back(conf.RESULT_API_URL, result)


def do_judge(submit_detail, submission_dir, submitted_executor):
    problem_id = submit_detail['problem_id']
    time_limit = submit_detail['time_limit']
    memory_limit = submit_detail['memory_limit']
    checker_type = submit_detail['checker_type']

    result = {
        "verdict": VerdictResult.AC,
        "desc": "",
        "time_usage": 0,
        "memory_usage": 0,
        "outputs": [],
    }

    case_no = 1
    while True:
        input_path = f'problems/{problem_id}/{case_no}.in'
        output_path = f'{submission_dir}/{case_no}.out'
        answer_path = f'problems/{problem_id}/{case_no}.ans'
        log_path = f'{submission_dir}/{case_no}.log'
        # processed all test cases
        if not os.path.isfile(input_path):
            break

        submitted_res = submitted_executor.execute(input_path, output_path, log_path, time_limit, memory_limit, trace=True)

        result['time_usage'] = max(result['time_usage'], submitted_res['timeused'])
        result['memory_usage'] = max(result['memory_usage'], submitted_res['memoryused'])
        with open(output_path, 'r') as f:
            result['outputs'].append(f.read())

        if submitted_res['result'] != VerdictResult.AC:
            result['verdict'] = submitted_res['result']
            result['desc'] = submitted_res.get('desc', '')
            return result

        # check the result
        checker = get_checker(checker_type)
        result['verdict'], info = checker.check(output_path, answer_path)

        if result['verdict'] != VerdictResult.AC:
            result['desc'] = info
            return result

        case_no += 1

    return result


def send_result_back(api_url, result):
    try:
        requests.post(api_url, result, timeout=3)
    except requests.exceptions.Timeout:
        logging.error(f'[send_result_back] soj has no response.')
