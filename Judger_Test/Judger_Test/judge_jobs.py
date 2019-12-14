import subprocess
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


def judge_submission(**submit_detail):
    result = do_judge(submit_detail)

    send_result_back(submit_detail['submit_id'], result)


def do_judge(submit_detail):
    submit_id = submit_detail['submit_id']
    problem_id = submit_detail['problem_id']
    submitted_code = submit_detail["submitted_code"]
    submitted_lang = submit_detail['submitted_lang']
    time_limit = submit_detail['time_limit']
    memory_limit = submit_detail['memory_limit']
    solution_code = submit_detail['solution_code']
    solution_lang = submit_detail['solution_lang']
    checker_type = submit_detail['checker_type']

    result = {
        "verdict": VerdictResult.AC.value,
        "desc": "",
        "time_usage": 0,
        "memory_usage": 0,
        "outputs": [],
    }

    try:
        submitted_executor = get_executor(submitted_lang, submitted_code)
    except ExecutorInitException as e:
        result.verdict = VerdictResult.CE.value
        result.desc = str(e)
        return result
    try:
        solution_executor = get_executor(solution_lang, solution_code)
    except ExecutorInitException as e:
        result.verdict = VerdictResult.SE.value
        result.desc = str(e)
        return result

    case_no = 1
    while True:
        input_path = f'problems/{problem_id}/{case_no}_in'  # TODO create parent directory
        output_path = f'problems/{problem_id}/{submit_id}/{case_no}_out'
        answer_path = f'problems/{problem_id}/{submit_id}/{case_no}_ans'

        # processed all test cases
        if not os.path.isfile(input_path):
            break

        submitted_res = submitted_executor.execute(time_limit, memory_limit, input_path, output_path)
        solution_res = solution_executor.execute(time_limit, memory_limit, input_path, answer_path)
        if solution_res['result'] != VerdictResult.AC:
            result['result'] = VerdictResult.SE
            result['desc'] = f'Solution has verdict <{RESULT_STR[solution_res["result"]]}> instead of <{RESULT_STR[VerdictResult.AC]}>'
            return result

        result['time_usage'] = max(result['time_usage'], submitted_res['timeused'])
        result['memory_usage'] = max(result['memory_usage'], submitted_res['memoryused'])
        with open(output_path, 'r') as f:
            result['outputs'].append(f.read())

        if submitted_res['result'] != VerdictResult.AC:
            result['result'] = submitted_res['result']
            return result

        # check the result
        checker = get_checker(checker_type)
        result['result'] = checker.check(output_path, answer_path, f'logs/{problem_id}_{submit_id}.log')

        if result['result'] != VerdictResult.AC:
            return result

        case_no += 1

    return result


def send_result_back(submit_id, result):
    try:
        requests.post(conf.RESULT_API_URL, {'submit_id': submit_id, 'result': result}, timeout=3)
    except requests.exceptions.Timeout:
        logging.error(f'[send_result_back] soj has no response.')
