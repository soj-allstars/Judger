from executors.base_executor import BaseExecutor
import lorun
from utils import create_file_to_write
from consts import VerdictResult
from exceptions import ExecutorInitException


class PythonExecutor(BaseExecutor):
    interpreter = None
    magic = None

    def init(self):
        code_path = f'{self.exe_dir}/code.py'
        with create_file_to_write(code_path) as code_file:
            code_file.write(self.code)

        exe_path = f'{self.exe_dir}/__pycache__/code.{self.magic}.pyc'
        self.exe_args = [self.interpreter, '-O', '-S', exe_path]

        log_path = f'{self.exe_dir}/compile.log'
        with open(log_path, 'w') as log_file:
            run_cfg = self.get_run_cfg(
                [self.interpreter, '-O', '-m', 'compileall', '-q', self.exe_dir],
                0,
                0,
                log_file.fileno(),
                runner=-1,
            )
            result = lorun.run(run_cfg)

        if result['result'] != VerdictResult.AC:
            with open(log_path, 'r') as log_file:
                raise ExecutorInitException(log_file.read())  # TODO check file size before read

    def get_additional_info(self, result, output_path, log_path):
        super().get_additional_info(result, output_path, log_path)
        if not log_path:
            return

        # Get the last line of log.
        with open(log_path, 'r') as f:
            lines = f.readlines()
            result['desc'] = result.get('desc', '') + (lines[-1] if lines else '')
