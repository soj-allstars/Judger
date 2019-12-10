import subprocess
import os
import sys
import conf
import requests
import logging
import lorun


fileName = "test.cpp"
cpFileName = r".\test.exe"
InputFile = ""
OutputFile = ""
YouFile = 'testdata/temp.out'

RESULT_STR = [
    'Accepted',
    'Presentation Error',
    'Time Limit Exceeded',
    'Memory Limit Exceeded',
    'Wrong Answer',
    'Runtime Error',
    'Output Limit Exceeded',
    'Compile Error',
    'System Error'
]


def set_input_file(name):
    global InputFile
    InputFile = name

def set_output_file(name):
    global OutputFile
    OutputFile = name


def run_one(p_path,in_path,out_path,time_limit,memory_limit):
    fin = open(in_path)
    ftemp = open(YouFile,'w')

    runcfg = {
        'args': [p_path],
        'fd_in': fin.fileno(),
        'fd_out': ftemp.fileno(),
        'timelimit': time_limit,  # in MS
        'memorylimit': memory_limit,  # in KB
    }
    rst = lorun.run(runcfg)
    fin.close()
    ftemp.close()
    print("run over --")

    if rst['result'] == 0:
        ftemp = open(YouFile)
        fout = open(out_path)
        #@todo check will change
        crst = lorun.check(fout.fileno(), ftemp.fileno())
        fout.close()
        ftemp.close()
        os.remove(YouFile)
        if crst != 0:
            rst['result'] = crst
            return rst

    return rst


def compile_code():
    #@todo control cp
    cp = subprocess.call(["g++", "-g", fileName, "-o", cpFileName])
    if cp != 0:
        print("compile error")
        return
    print("cp over ---")


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
    code_file = open(fileName, "w")
    code_file.write(submit_detail["submitted_code"])
    code_file.close()

    init()
    compile_code()

    # ------
    in_path = os.path.join("testdata","1.in")
    out_path = os.path.join("testdata","1.out")
    rst = run_one(cpFileName,in_path,out_path,
                  submit_detail["time_limit"],submit_detail["memory_limit"])
    #-------
    result = dict()
    result["verdict"] = rst["result"]
    result["time_usage"] = rst["timeused"]
    result["memory_usage"] = rst["memoryused"]
    result["desc"] = get_optional()

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

# if __name__ == '__main__':
#     init()
#     in_path = os.path.join("testdata", "1.in")
#     out_path = os.path.join("testdata", "1.out")
#     rst = run_one(cpFileName, in_path, out_path,
#                   3000, 300000)
#     result = dict()
#     result["verdict"] = rst["result"]
#     result["time_usage"] = rst["timeused"]
#     result["memory_usage"] = rst["memoryused"]
#     result["desc"] = get_optional()
#
#     result["outputs"] = [
#         "fuck people1",
#         "fuck people2"
#     ]
#     print(result)
#     print("deal OK!")