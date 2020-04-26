import unittest
from judge_jobs import do_judge
from executors import get_executor
from consts import VerdictResult
import exceptions
import shutil
import conf


class TestGcc(unittest.TestCase):
    submission_lang = "GCC"
    submission_dir = f'{conf.PROJECT_ROOT}/executors/tests/problems/1/test'

    def test_AC(self):
        ac_code = """
#include<stdio.h>
int main() {
    int a, b;
    scanf("%d%d",&a,&b);
    printf("%d",a+b);
    return 0;
}
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
           #include<stdio.h>
int main() {
    int a, b;
    scanf("%d%d",&a,&b);
    printf("%d",a+b+1);
    return 0;
}
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
#include<stdio.h>
int main() {
    int a, b;
    scanf("%d%d",&a,&b);
    while(1) {a+=b;}
    printf("%d",a+b);
    return 0;
}
"""
        submitted_executor = get_executor(self.submission_lang, tle_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1111,
            "memory_limit": 262144,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)

        self.assertEqual(result["verdict"], VerdictResult.TLE, msg=result['desc'])

    def test_MLE(self):
        mle_code = """
            #include <stdio.h>
            int fuck[3500000];
            int dick[3500000];
            int main() {
                int a, b;
                scanf("%d%d",&a,&b);
                for(int i = 0;i < 3500000;i++)
                { fuck[i] = i;
                dick[i] = i;}
                printf("%d",fuck[1]+dick[1]);
                return 0;
            }
"""
        submitted_executor = get_executor(self.submission_lang, mle_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 10011,
            "memory_limit": 28072,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)

        self.assertEqual(result["verdict"], VerdictResult.MLE, msg=f"{result}\n{result['desc']}")

    def test_RE(self):
        re_code = """
            #include <stdio.h>
            int fuck[3500000];
            int dick[3500000];
            int main() {
                int a, b;
                scanf("%d%d",&a,&b);
                for(int i = 0;i < 4000000;i++)
                { fuck[i] = i;
                dick[i] = i;}
                printf("%d",fuck[1]+dick[1]);
                return 0;
            }
"""
        submitted_executor = get_executor(self.submission_lang, re_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1111,
            "memory_limit": 262144,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)

        self.assertEqual(result["verdict"], VerdictResult.RE, msg=result['desc'])

    def test_CE(self):
        ce_code = """
            #include <stdio.h>
            int fuck[3500000];
            int dick[3500000];
            int main() {
                int a, b;
                scanf("%d%d",&a,&b);
                for(int i = 0;i < 4000000;i++)
                { fuck[i] = i
                dick[i] = i;}
                printf("%d",fuck[1]+dick[1]);
                return 0;
            }
"""
        with self.assertRaises(exceptions.ExecutorInitException) as cm:
            submitted_executor = get_executor(self.submission_lang, ce_code, f'{self.submission_dir}/submitted')
            print(cm.exception, flush=True)

    def test_OLE(self):
        ole_code = f"""
                    #include <stdio.h>
                    int main() {{
                        int a, b;
                        scanf("%d%d",&a,&b);
                        for(int i = 0;i < 729145;i++)
                            printf("%s","{'A' * 100}");
                            
                        return 0;
                    }}
"""
        submitted_executor = get_executor(self.submission_lang, ole_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 22222,
            "memory_limit": 262144,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)

        self.assertEqual(result["verdict"], VerdictResult.OLE, msg=result['desc'])

    def tearDown(self) -> None:
        shutil.rmtree(self.submission_dir, ignore_errors=True)
