import unittest
import conf
from judge_jobs import do_judge
from executors import get_executor
from consts import VerdictResult


class TestCpy(unittest.TestCase):
    solution_code = """
a = input().split()
print(int(a[0]) + int(a[1]))
    """
    solution_lang = "CPY"

    def test_AC(self):
        submission_dir = f'problems/1/test'
        ac_code = """
a = input().split()
print(int(a[0]) + int(a[1]))
        """
        submitted_executor = get_executor("CPY", ac_code, f'{submission_dir}/submitted')
        solution_executor = get_executor(self.solution_lang, self.solution_code, f'{submission_dir}/solution')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1000,
            "memory_limit": 131072,
            "checker_type": "icmp",
        }, submission_dir, submitted_executor, solution_executor)

        self.assertEqual(result['verdict'], VerdictResult.AC)
