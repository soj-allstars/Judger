from executors.base_executor import BaseExecutor
import lorun
from utils import create_file_to_write
from consts import VerdictResult
from exceptions import ExecutorInitException


class GccExecutor(BaseExecutor):
    lang = 'GCC'

    def init(self):
        code_path = f'{self.exe_dir}/code.c'
        code_file = create_file_to_write(code_path)
        code_file.write(self.code)
        code_file.close()

        exe_path = f'{self.exe_dir}/executable'
        log_path = f'{self.exe_dir}/compile.log'
        self.exe_args = [exe_path]

        with open(log_path, 'w') as log_file:
            run_cfg = self.get_run_cfg(
                ['gcc', code_path, '-DONLINE_JUDGE', '-o', exe_path, '-Wall', '-O2', '-std=c11'],
                0,
                0,
                log_file.fileno(),
                runner=-1,
            )
            result = lorun.run(run_cfg)

        if result['result'] != VerdictResult.AC:
            with open(log_path, 'r') as log_file:
                raise ExecutorInitException(log_file.read())
