import subprocess
import os
import sys
import conf
import requests
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


def judge_submission(**submit_detail):
    result = dict()
    code_file = open(fileName, "w")
    code_file.write(submit_detail["submitted_code"])
    code_file.close()

    init()
    compile_code()
    result["verdict"] = compared_with_answer()
    result["desc"] = get_optional()
    result["time_usage"] = 0
    result["memory_usage"] = 0
    result["outputs"] = [
        "fuck people1",
        "fuck people2"
    ]
    print("deal OK!")

    send_result_back(submit_detail['submit_id'], result)


def send_result_back(submit_id, result):
    try:
        requests.post(conf.RESULT_API_URL, {'submit_id': submit_id, 'result': result}, timeout=0.01)
    except requests.exceptions.Timeout:
        logging.error(f'[send_result_back] soj has no response.')
