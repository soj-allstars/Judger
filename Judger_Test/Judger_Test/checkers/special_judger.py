import os
from executors.base_executor import BaseExecutor
from conf import CHECKER_DIR


class SpecialJudgeSpawner(BaseExecutor):
    lang = 'GXX'

    def __init__(self, code, exe_dir, name):
        super().__init__(code, exe_dir)
        self.code_file_path = f'checkers/{name}.cpp'
        self.checker_exec = f'{CHECKER_DIR}/{name}'

    def init(self):
        with open(self.code_file_path, 'w') as f:
            f.write(self.code)

        self.exe_args = ['g++', self.code_file_path, '-o', self.checker_exec, '-I', 'testlib/', '-O2']

    def cleanup(self):
        if os.path.exists(self.code_file_path):
            os.remove(self.code_file_path)
