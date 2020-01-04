import lorun
import os
from consts import VerdictResult

def create_special_judger(**sj_detail):
    code = sj_detail['sj_code']
    name = sj_detail['sj_name']
    code_file_path = './'+name+'.cpp'
    log_file_path = './sj_logs/'+name+'_log.txt'
    checker_exec = '../testlib/bin/' + name
    try:
        with open(code_file_path, 'w') as cf:
            cf.write(code)

        with open(log_file_path, 'w') as log_file:
            run_cfg = {
                'args': ['g++', code_file_path, '-o', checker_exec, '-I', '../testlib/'],
                'fd_in': 0,
                'fd_out': 0,
                'fd_err': log_file.fileno(),
                'timelimit': 5000,  # 5 S
                'memorylimit': 251072,
            }
            result = lorun.run(run_cfg)
            # print(result)
            feedback = dict()
            feedback['log'] = log_file.read()
            feedback['result'] = result['result']

            # TODO send_result_back
            if result['result'] != VerdictResult.AC:
                pass
            else:
                pass
    except Exception:
        # TODO send_result_back
        pass
    finally:
        if os.path.exists(code_file_path):
            os.remove(code_file_path)
        #os.remove(log_file_path)


# a test

# if __name__ == '__main__':
#     sj_detail = dict()
#     sj_detail['sj_code'] = '''
# #include <iostream>
# #include"testlib.h"
# using namespace std;
# int main()
# {
#     cout << "1111" <<endl;
# }
#
#     '''
#     sj_detail['sj_name'] = 'fuck'
#     create_special_judger(**sj_detail)
