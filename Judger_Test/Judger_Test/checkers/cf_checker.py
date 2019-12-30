from conf import CHECKER_DIR
from consts import VerdictResult
import subprocess


class CFChecker:
    def __init__(self, checker_type):
        self.exe = f'{CHECKER_DIR}/{checker_type}'

    def check(self, output_file, answer_file):
        exe_args = [self.exe, "foo", output_file, answer_file]
        cp = subprocess.run(exe_args, capture_output=True)

        if cp.returncode != 0:
            return VerdictResult.WA, str(cp.stderr)  # stderr

        return VerdictResult.AC, str(cp.stderr)
