from executors.base_executor import BaseExecutor
from utils import create_file_to_write


class PypyExecutor(BaseExecutor):
    def init(self):
        code_path = f'{self.exe_dir}/code.py'
        code_file = create_file_to_write(code_path)
        code_file.write(self.code)
        code_file.close()
        # 本质其实是赋值 exe_args ? --lyw
        self.exe_args = ["pypy3", code_path]
        self.lang = 'PYPY'

    def get_additional_info(self, result, output_path, log_path):
        # Get last line of log. Maybe will be modified later.
        if not log_path:
            return

        with open(log_path, 'r') as f:
            lines = f.readlines()
            result['desc'] = lines[-1] if lines else ''
