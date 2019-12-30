import unittest
# import conf
from judge_jobs import do_judge
from executors import get_executor
from consts import VerdictResult
import exceptions

class TestGxx(unittest.TestCase):
    solution_code = """
#include <iostream>
using namespace std;
int main() {
    int a, b;
    cin >> a >> b;
    cout << a + b << endl;
    return 0;
}
    """
    solution_lang = "GXX"
    submission_lang = "GXX"

    def test_AC(self):
        submission_dir = f'problems/1/test'
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
        submitted_executor = get_executor("GXX", ac_code, f'{submission_dir}/submitted')
        solution_executor = get_executor(self.solution_lang, self.solution_code, f'{submission_dir}/solution')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1000,
            "memory_limit": 100072,
            "checker_type": "icmp",
        }, submission_dir, submitted_executor, solution_executor)

        self.assertEqual(result['verdict'], VerdictResult.AC)

    def test_WA(self):
        submission_dir = f'problems/1/test'
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
        submitted_executor = get_executor("GXX", wa_code, f'{submission_dir}/submitted')
        solution_executor = get_executor(self.solution_lang, self.solution_code, f'{submission_dir}/solution')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1000,
            "memory_limit": 131072,
            "checker_type": "icmp",
        }, submission_dir, submitted_executor, solution_executor)
        self.assertEqual(result['verdict'], VerdictResult.WA)

    def test_TLE(self):
        submission_dir = f'problems/1/test'
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
        submitted_executor = get_executor(self.submission_lang, tle_code, f'{submission_dir}/submitted')
        solution_executor = get_executor(self.solution_lang, self.solution_code, f'{submission_dir}/solution')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1111,
            "memory_limit": 131072,
            "checker_type": "icmp",
        }, submission_dir, submitted_executor, solution_executor)
        self.assertEqual(result["verdict"], VerdictResult.TLE)

    def test_MLE(self):
        submission_dir = f'problems/1/test'
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
        submitted_executor = get_executor(self.submission_lang, mle_code, f'{submission_dir}/submitted')
        solution_executor = get_executor(self.solution_lang, self.solution_code, f'{submission_dir}/solution')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 10011,
            "memory_limit": 26072,
            "checker_type": "icmp",
        }, submission_dir, submitted_executor, solution_executor)
        self.assertEqual(result["verdict"], VerdictResult.MLE)

    def test_RE(self):
        submission_dir = f'problems/1/test'
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
        submitted_executor = get_executor(self.submission_lang, re_code, f'{submission_dir}/submitted')
        solution_executor = get_executor(self.solution_lang, self.solution_code, f'{submission_dir}/solution')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1111,
            "memory_limit": 306072,
            "checker_type": "icmp",
        }, submission_dir, submitted_executor, solution_executor)
        print(result)
        self.assertEqual(result["verdict"], VerdictResult.RE)

    def test_SE(self):
        submission_dir = f'problems/1/test'
        re_code = """
            #include <iostream>
            int fuck[60000000];
            using namespace std;
            int main() {
                int a, b;
                cin >> a >> b;
                for(int i = 0;i < 60005000;i++)
                { fuck[i] = i;
                }
                cout << a + b << endl;
                return 0;
            }
        """
        submitted_executor = get_executor(self.submission_lang, re_code, f'{submission_dir}/submitted')
        solution_executor = get_executor(self.solution_lang, self.solution_code, f'{submission_dir}/solution')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1111,
            "memory_limit": 306072,
            "checker_type": "icmp",
        }, submission_dir, submitted_executor, solution_executor)
        print(result)
        self.assertEqual(result["verdict"], VerdictResult.RE)

    def test_CE(self):
        submission_dir = f'problems/1/test'
        re_code = """
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
        with self.assertRaises(exceptions.ExecutorInitException):
            submitted_executor = get_executor(self.submission_lang, re_code, f'{submission_dir}/submitted')
