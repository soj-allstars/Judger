import subprocess
import os
import sys
import conf
import requests
from rq import get_current_job
import logging


fileName = "test.cpp"
cpFileName = r".\test.exe"


def compile_code():
    subprocess.call(["g++", "-g", fileName, "-o", cpFileName])
    print("cp over ---")

    with open('output.txt', 'w') as Out_f:
        p = subprocess.Popen([cpFileName], stdout=Out_f)
        p.communicate()
    print("run over --")


def compared_with_answer():
    with open('output.txt', 'r') as Out_f:
        with open('answer.txt', 'r') as Ans_f:
            out = Out_f.read()
            ans = Ans_f.read()
            if out == ans:
                print("true")
                return 0
            else:
                print("false")
                return 1


def init():
    init_by_os()


def init_by_os():
    global cpFileName
    my_os = sys.platform
    if "linux" == my_os:
        cpFileName = r"./test.out"


def get_optional():
    # Todo
    return "fuck"


def deal_submitted(**submit_detail):
    """for 'judge' queue"""
    dict_to_return = dict()
    code_file = open(fileName, "w")
    code_file.write(submit_detail["submitted_code"])
    code_file.close()

    init()
    compile_code()
    dict_to_return["verdict"] = compared_with_answer()
    dict_to_return["desc"] = get_optional()
    dict_to_return["time_usage"] = 0
    dict_to_return["memory_usage"] = 0
    dict_to_return["outputs"] = [
        "fuck people1",
        "fuck people2"
    ]
    print("deal OK!")
    return dict_to_return


def send_result_back(submit_id):
    """for 'result' queue"""
    judge_job = get_current_job().dependency
    result = judge_job.result
    if not result:
        logging.error(f'[send_result_back] job has not finished. {judge_job.id=}')

    try:
        requests.post(conf.SOJ_HOST, {'sub_id': submit_id, 'result': result}, timeout=0.01)
    except requests.exceptions.Timeout:
        logging.error(f'[send_result_back] soj has no response.')
