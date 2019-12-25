from executors.base_executor import BaseExecutor
import lorun
from utils import create_file_to_write
from consts import VerdictResult
from exceptions import ExecutorInitException


class CpyExecutor(BaseExecutor):
    def init(self):
        code_path = f'{self.exe_dir}/code.py'
        code_file = create_file_to_write(code_path)
        code_file.write(self.code)
        code_file.close()
        # 本质其实是赋值 exe_args ? --lyw
        self.exe_args = ["python", code_path]