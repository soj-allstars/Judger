import unittest
import conf
from judge_jobs import do_judge
from executors import get_executor
from consts import VerdictResult
from judge_jobs import create_special_judge
import shutil


class TestSpecialJudger(unittest.TestCase):
    submission_dir = f'{conf.PROJECT_ROOT}/executors/tests/problems/1/test'
    checker_exec = None

    def test_SJ(self):
        sj_code = """
#include "testlib.h"
#include <stdio.h>

int main(int argc, char * argv[])
{
    setName("compare two signed int%d's", 8 * int(sizeof(int)));
    registerTestlibCmd(argc, argv);
    
    int ja = ans.readInt();
    int pa = ouf.readInt();
    
    if (ja != pa)
        quitf(_wa, "expected %d, found %d", ja, pa);
    
    quitf(_ok, "answer is %d", ja);
}
"""
        ac_code = """
                #include <iostream>
                using namespace std;
                int main() {
                    int a, b;
                    cin >> a >> b;
                    cout << a + b<< endl;
                    return 0;
                }
        """

        sj_name = 'test_checker'
        log_file_path = f'{conf.LOG_DIR}/sj_{sj_name}.log'

        result = create_special_judge(sj_code, sj_name, log_file_path)
        self.assertEqual(result['result'], VerdictResult.AC, msg=result['desc'])

        submitted_executor = get_executor("GXX", ac_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1000,
            "memory_limit": 262144,
            "checker_type": sj_name,
        }, self.submission_dir, submitted_executor)
        self.assertEqual(result['verdict'], VerdictResult.AC, msg=result['desc'])

    def tearDown(self) -> None:
        shutil.rmtree(self.submission_dir, ignore_errors=True)
