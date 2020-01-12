import unittest
import conf
from judge_jobs import do_judge
from executors import get_executor
from consts import VerdictResult
import shutil


class TestCpy(unittest.TestCase):
    solution_code = """
a = input().split()
print(int(a[0]) + int(a[1]))
    """
    solution_lang = "CPY"
    submission_lang = "CPY"

    submission_dir = f'problems/1/test'

    def test_AC(self):
        self.submission_dir = f'problems/1/test'
        ac_code = """
a = input().split()
print(int(a[0]) + int(a[1]))
        """
        submitted_executor = get_executor(self.submission_lang, ac_code, f'{self.submission_dir}/submitted')
        solution_executor = get_executor(self.solution_lang, self.solution_code, f'{self.submission_dir}/solution')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1000,
            "memory_limit": 131072,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor, solution_executor)
        self.assertEqual(result['verdict'], VerdictResult.AC)

    def test_WA(self):
        self.submission_dir = f'problems/1/test'
        ac_code = """
a = input().split()
print(int(a[0]) + int(a[1])+1)
                """
        submitted_executor = get_executor(self.submission_lang, ac_code, f'{self.submission_dir}/submitted')
        solution_executor = get_executor(self.solution_lang, self.solution_code, f'{self.submission_dir}/solution')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1000,
            "memory_limit": 131072,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor, solution_executor)
        print(result['desc'])

        self.assertEqual(result['verdict'], VerdictResult.WA)

    def test_TLE(self):
        self.submission_dir = f'problems/1/test'
        ac_code = """
a = input().split()
while 1:
    a[1] = int(a[1]) + 1
print(int(a[0]) + int(a[1])+1)
                        """
        submitted_executor = get_executor(self.submission_lang, ac_code, f'{self.submission_dir}/submitted')
        solution_executor = get_executor(self.solution_lang, self.solution_code, f'{self.submission_dir}/solution')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1000,
            "memory_limit": 131072,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor, solution_executor)
        print(result['desc'])

        self.assertEqual(result['verdict'], VerdictResult.TLE)

    def test_RE(self):
        self.submission_dir = f'problems/1/test'
        ac_code = """
a = input().split()
a = a + 1
print(int(a[0]) + int(a[1])+1)
                                """
        submitted_executor = get_executor(self.submission_lang, ac_code, f'{self.submission_dir}/submitted')
        solution_executor = get_executor(self.solution_lang, self.solution_code, f'{self.submission_dir}/solution')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1000,
            "memory_limit": 131072,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor, solution_executor)
        print(result['desc'])

        self.assertEqual(result['verdict'], VerdictResult.RE)

# MemoryError still RE see log
    def test_MLE(self):
        self.submission_dir = f'problems/1/test'
        ac_code = """
a = input().split()
a =[i for i in range(0, 10000000)]
print(int(a[0]) + int(a[1])+1)
                                        """
        solution_executor = get_executor(self.solution_lang, self.solution_code, f'{self.submission_dir}/solution')
        submitted_executor = get_executor(self.submission_lang, ac_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1000,
            "memory_limit": 131072,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor, solution_executor)
        print(result['desc'])

        self.assertEqual(result['verdict'], VerdictResult.RE)

    def tearDown(self) -> None:
        shutil.rmtree(self.submission_dir, ignore_errors=True)