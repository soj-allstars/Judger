import unittest
from judge_jobs import do_judge
from executors import get_executor
from consts import VerdictResult
import exceptions
import shutil


class TestGcc(unittest.TestCase):
    submission_lang = "GCC"
    submission_dir = f'problems/1/test'

    def test_AC(self):
        self.submission_dir = f'problems/1/test'
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

        self.assertEqual(result['verdict'], VerdictResult.AC)

    def test_WA(self):
        self.submission_dir = f'problems/1/test'
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
        print(result['desc'])

        self.assertEqual(result['verdict'], VerdictResult.WA)

    def test_TLE(self):
        self.submission_dir = f'problems/1/test'
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
        print(result['desc'])

        self.assertEqual(result["verdict"], VerdictResult.TLE)

    def test_MLE(self):
        self.submission_dir = f'problems/1/test'
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
        print(result)
        print(result['desc'])

        self.assertEqual(result["verdict"], VerdictResult.MLE)

    def test_RE(self):
        self.submission_dir = f'problems/1/test'
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
        print(result['desc'])

        self.assertEqual(result["verdict"], VerdictResult.RE)

    def test_CE(self):
        self.submission_dir = f'problems/1/test'
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
            print(cm.exception)

    def test_OLE(self):
        self.submission_dir = f'problems/1/test'
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
        print(result['desc'])

        self.assertEqual(result["verdict"], VerdictResult.OLE)

    def tearDown(self) -> None:
        shutil.rmtree(self.submission_dir, ignore_errors=True)
