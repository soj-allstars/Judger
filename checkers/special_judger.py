import os
from executors.base_executor import BaseExecutor
from conf import CHECKER_DIR


class SpecialJudgeSpawner(BaseExecutor):
    lang = 'GXX'

    def __init__(self, code, exe_dir, name):
        self.code_file_path = f'{CHECKER_DIR}/{name}.cpp'
        self.checker_exec = f'{CHECKER_DIR}/{name}'
        super().__init__(code, exe_dir)

    def init(self):
        with open(self.code_file_path, 'w') as f:
            f.write(self.code)

        self.exe_args = ['g++', self.code_file_path, '-o', self.checker_exec, '-O2', '-I', f'{CHECKER_DIR}']

    def get_additional_info(self, result, output_path, log_path):
        super().get_additional_info(result, output_path, log_path)
        if not log_path:
            return

        with open(log_path, 'r') as f:
            result['desc'] = f.read()

    def cleanup(self, log_path):
        super().cleanup(log_path)
        if os.path.exists(self.code_file_path):
            os.remove(self.code_file_path)


def create_special_judge(sj_code, sj_name, log_path, time_limit=10000, memory_limit=256 * 1024, trace=False):
    sj_spawner = SpecialJudgeSpawner(sj_code, None, sj_name)
    return sj_spawner.execute(None, None, log_path, time_limit, memory_limit, trace=trace)  # compile here
