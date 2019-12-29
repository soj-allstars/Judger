from executors.base_executor import BaseExecutor
import lorun
from utils import create_file_to_write
from consts import VerdictResult
from exceptions import ExecutorInitException


class GxxExecutor(BaseExecutor):
    def init(self):
        code_path = f'{self.exe_dir}/code.cpp'
        code_file = create_file_to_write(code_path)
        code_file.write(self.code)
        code_file.close()

        exe_path = f'{self.exe_dir}/executable'
        log_path = f'{self.exe_dir}/compile.log'
        with open(log_path, 'w') as log_file:
            run_cfg = {
                'args': ['g++', code_path, '-o', exe_path, '-O2', '--std=c++14'],
                'fd_in': 0,
                'fd_out': 0,
                'fd_err': log_file.fileno(),
                'timelimit': 5000,  # 5 S
                'memorylimit': 131072,  # 64 MB
            }
            result = lorun.run(run_cfg)

        if result['result'] != VerdictResult.AC:
            with open(log_path, 'r') as log_file:
                raise ExecutorInitException(log_file.read())

        self.exe_args = [exe_path]
