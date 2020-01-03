import os
import sys
import conf
import requests
import logging
import lorun
from consts import VerdictResult, RESULT_STR
from exceptions import ExecutorInitException
from executors import get_executor
from checkers import get_checker
import json


def judge_submission(**submit_detail):
    submitted_code = submit_detail["submitted_code"]
    submitted_lang = submit_detail['submitted_lang']
    solution_code = submit_detail['solution_code']
    solution_lang = submit_detail['solution_lang']
    submit_id = submit_detail['submit_id']
    problem_id = submit_detail['problem_id']

    result = {
        "verdict": VerdictResult.SE,
        "desc": "",
        "time_usage": 0,
        "memory_usage": 0,
        "outputs": [],
    }

    try:
        submission_dir = f'problems/{problem_id}/{submit_id}'
        try:
            submitted_executor = get_executor(submitted_lang, submitted_code, f'{submission_dir}/submitted')
        except ExecutorInitException as e:
            result['verdict'] = VerdictResult.CE
            result['desc'] = str(e)
            return result
        try:
            solution_executor = get_executor(solution_lang, solution_code, f'{submission_dir}/solution')
        except ExecutorInitException as e:
            result['verdict'] = VerdictResult.SE
            result['desc'] = str(e)
            return result
        result = do_judge(submit_detail, submission_dir, submitted_executor, solution_executor)
    finally:
        send_result_back(submit_id, result)


def do_judge(submit_detail, submission_dir, submitted_executor, solution_executor):
    submit_id = submit_detail['submit_id']
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
        input_path = f'problems/{problem_id}/{case_no}_in'
        output_path = f'{submission_dir}/{case_no}_out'
        answer_path = f'{submission_dir}/{case_no}_ans'
        log_path = f'{submission_dir}/{case_no}_log'
        # processed all test cases
        if not os.path.isfile(input_path):
            break

        solution_res = solution_executor.execute(input_path, answer_path, log_path, time_limit, memory_limit)
        submitted_res = submitted_executor.execute(input_path, output_path, log_path, time_limit, memory_limit)
        if solution_res['result'] != VerdictResult.AC:
            result['verdict'] = VerdictResult.SE
            result['desc'] = f'Solution has verdict <{RESULT_STR[solution_res["result"]]}> instead of <{RESULT_STR[VerdictResult.AC]}>'
            return result

        result['time_usage'] = max(result['time_usage'], submitted_res['timeused'])
        result['memory_usage'] = max(result['memory_usage'], submitted_res['memoryused'])
        with open(output_path, 'r') as f:
            result['outputs'].append(f.read())

        if submitted_res['result'] != VerdictResult.AC:
            result['verdict'] = submitted_res['result']
            return result

        # check the result
        checker = get_checker(checker_type)
        result['verdict'], info = checker.check(output_path, answer_path)

        if result['verdict'] != VerdictResult.AC:
            result['desc'] = info
            return result

        case_no += 1

    return result


def send_result_back(submit_id, result):
    try:
        requests.post(conf.RESULT_API_URL, {'submit_id': submit_id, 'result': json.dumps(result)}, timeout=3)
    except requests.exceptions.Timeout:
        logging.error(f'[send_result_back] soj has no response.')
