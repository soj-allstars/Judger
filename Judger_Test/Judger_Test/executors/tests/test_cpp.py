import unittest
import conf
from judge_jobs import do_judge
from executors import get_executor
from consts import VerdictResult


class TestCpp(unittest.TestCase):
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
    solution_lang = "G++"

    def test_AC(self):
        submission_dir = f'problems/1/test'
        ac_code = """
#include <iostream>
using namespace std;
int main() {
    int a, b;
    cin >> a >> b;
    cout << a + b << endl;
    return 0;
}
        """
        submitted_executor = get_executor("G++", ac_code, f'{submission_dir}/submitted')
        solution_executor = get_executor(self.solution_lang, self.solution_code, f'{submission_dir}/solution')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1000,
            "memory_limit": 131072,
            "checker_type": "icmp",
        }, submission_dir, submitted_executor, solution_executor)

        self.assertEqual(result['verdict'], VerdictResult.AC)
