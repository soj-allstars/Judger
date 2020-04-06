import unittest
from judge_jobs import do_judge
from executors import get_executor
from consts import VerdictResult
import exceptions
import shutil
import conf


class TestGxx(unittest.TestCase):
    submission_lang = "GXX"
    submission_dir = f'{conf.PROJECT_ROOT}/executors/tests/problems/1/test'

    def test_AC(self):
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
        submitted_executor = get_executor("GXX", ac_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1000,
            "memory_limit": 262144,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)

        self.assertEqual(result['verdict'], VerdictResult.AC)

    def test_WA(self):
        wa_code = """
            #include <iostream>
            using namespace std;
            int main() {
                int a, b;
                cin >> a >> b;
                cout << a + b + 2 << endl;
                return 0;
            }
"""
        submitted_executor = get_executor("GXX", wa_code, f'{self.submission_dir}/submitted')
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
        tle_code = """
            #include <iostream>
            using namespace std;
            int main() {
                int a, b;
                cin >> a >> b;
                while(true){
                    a += b;
                }
                cout << a + b << endl;
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
        mle_code = """
            #include <iostream>
            int fuck[3000000];
            int dick[3000000];
            using namespace std;
            int main() {
                int a, b;
                cin >> a >> b;
                for(int i = 0;i < 3000000;i++)
                { fuck[i] = i;
                dick[i] = i;}
                cout << a + b << endl;
                return 0;
            }
"""
        submitted_executor = get_executor(self.submission_lang, mle_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 10011,
            "memory_limit": 26072,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])

        self.assertEqual(result["verdict"], VerdictResult.MLE)

    def test_RE(self):
        re_code = """
            #include <iostream>
            int fuck[60000];
            using namespace std;
            int main() {
                int a, b;
                cin >> a >> b;
                for(int i = 0;i < 65000;i++)
                { fuck[i] = i;
                }
                cout << a + b << endl;
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
        ce_code = """
            #include <iostream>
            int fuck[60000000000];
            using namespace std;
            int main() {
                int a, b;
                cin >> a >> b;
                for(int i = 0;i < 60050000000;i++)
                { fuck[i] = i;
               }
                cout << a + b << endl;
                return 0;
            }
"""
        with self.assertRaises(exceptions.ExecutorInitException) as cm:
            submitted_executor = get_executor(self.submission_lang, ce_code, f'{self.submission_dir}/submitted')
            print(cm.exception)

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
        print(result['desc'])

        self.assertEqual(result["verdict"], VerdictResult.OLE)

    def tearDown(self) -> None:
        shutil.rmtree(self.submission_dir, ignore_errors=True)
