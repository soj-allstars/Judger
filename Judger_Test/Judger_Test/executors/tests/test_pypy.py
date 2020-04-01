import unittest
from judge_jobs import do_judge
from executors import get_executor
from consts import VerdictResult
import shutil


class TestPypy(unittest.TestCase):
    submission_lang = "PYPY"
    submission_dir = f'problems/1/test'

    def test_AC(self):
        self.submission_dir = f'problems/1/test'
        ac_code = """
a = input().split()
print(int(a[0]) + int(a[1]))
"""
        submitted_executor = get_executor(self.submission_lang, ac_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1000,
            "memory_limit": 262144,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        self.assertEqual(result['verdict'], VerdictResult.AC)

    def test_WA(self):
        self.submission_dir = f'problems/1/test'
        wa_code = """
a = input().split()
print(int(a[0]) + int(a[1])+1)
"""
        submitted_executor = get_executor(self.submission_lang, wa_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1000,
            "memory_limit": 262144,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])

        self.assertEqual(result['verdict'], VerdictResult.WA)

    def test_TLE(self):
        self.submission_dir = f'problems/1/test'
        tle_code = """
a = input().split()
while 1:
    a[1] = int(a[1]) + 1
print(int(a[0]) + int(a[1])+1)
"""
        submitted_executor = get_executor(self.submission_lang, tle_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 500,
            "memory_limit": 262144,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])

        self.assertEqual(result['verdict'], VerdictResult.TLE)

    def test_RE(self):
        self.submission_dir = f'problems/1/test'
        re_code = """
a = input().split()
a = a + 1
print(int(a[0]) + int(a[1])+1)
"""
        submitted_executor = get_executor(self.submission_lang, re_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1000,
            "memory_limit": 262144,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])

        self.assertEqual(result['verdict'], VerdictResult.RE)

    def test_MLE(self):
        self.submission_dir = f'problems/1/test'
        mle_code = """
a = input().split()
a =[i for i in range(0, 100000000)]
print(int(a[0]) + int(a[1])+1)
"""
        submitted_executor = get_executor(self.submission_lang, mle_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1000,
            "memory_limit": 262144,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])

        self.assertEqual(result['verdict'], VerdictResult.MLE)

    def test_OLE(self):
        self.submission_dir = f'problems/1/test'
        ole_code = f"""
a = input().split()
for i in range(0, 729145):
    print("{'A' * 100}")
"""
        submitted_executor = get_executor(self.submission_lang, ole_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 22222,
            "memory_limit": 262144,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])

        self.assertEqual(result['verdict'], VerdictResult.OLE)

    def tearDown(self) -> None:
        shutil.rmtree(self.submission_dir, ignore_errors=True)
