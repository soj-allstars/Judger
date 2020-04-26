import unittest
from judge_jobs import do_judge
from executors import get_executor
from consts import VerdictResult
import shutil
import conf


# TODO: we need to create problem input files in test, put them under problems/0, and delete it after test finished
class TestCpy(unittest.TestCase):
    submission_lang = "CPY"
    submission_dir = f'{conf.PROJECT_ROOT}/executors/tests/problems/1/test'

    def test_AC(self):
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
        self.assertEqual(result['verdict'], VerdictResult.AC, msg=result['desc'])

    def test_WA(self):
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

        self.assertEqual(result['verdict'], VerdictResult.WA, msg=result['desc'])

    def test_TLE(self):
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
            "time_limit": 1000,
            "memory_limit": 262144,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)

        self.assertEqual(result['verdict'], VerdictResult.TLE, msg=result['desc'])

    def test_RE(self):
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

        self.assertEqual(result['verdict'], VerdictResult.RE, msg=result['desc'])

    @unittest.skip("cpy MLE is really weird that memory_used is slightly lower than memory_limit, "
                   "resulting in RE instead of MLE. maybe it's lorun's issue")
    def test_MLE(self):
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

        self.assertEqual(result['verdict'], VerdictResult.MLE, msg=result['desc'])

    def test_OLE(self):
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

        self.assertEqual(result['verdict'], VerdictResult.OLE, msg=result['desc'])

    def tearDown(self) -> None:
        shutil.rmtree(self.submission_dir, ignore_errors=True)
