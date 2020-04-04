import unittest
import conf
from judge_jobs import do_judge
from executors import get_executor
from consts import VerdictResult
import shutil
import exceptions


class TestJava(unittest.TestCase):
    submission_lang = "JAVA"
    submission_dir = f'{conf.PROJECT_ROOT}/executors/tests/problems/1/test'

    def test_AC(self):
        ac_code = """
import java.util.Scanner;
public class Solution {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt(),b=sc.nextInt();
        System.out.println(a+b);
    }
}
"""
        submitted_executor = get_executor(self.submission_lang, ac_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 5000,
            "memory_limit": 262144,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])
        self.assertEqual(result['verdict'], VerdictResult.AC)

    def test_WA(self):
        wa_code = """
        import java.util.Scanner;
        public class Solution {
            public static void main(String[] args) {
                Scanner sc=new Scanner(System.in);
                int a=sc.nextInt(),b=sc.nextInt();
                System.out.println(a+b+1);
            }
        }
"""
        submitted_executor = get_executor(self.submission_lang, wa_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 5000,
            "memory_limit": 262144,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])
        self.assertEqual(result['verdict'], VerdictResult.WA)

    def test_CE(self):
        ce_code = """
        import java.util.Scanner;
        public class Solution {
            public static void main(String[] args) {
                Scanner sc=new Scanner(System.in);
                int a=sc.nextInt(),b=sc.nextInt()
                System.out.println(a+b+1);
            }
        }
"""
        with self.assertRaises(exceptions.ExecutorInitException) as cm:
            submitted_executor = get_executor(self.submission_lang, ce_code, f'{self.submission_dir}/submitted')
            print(cm.exception)

    def test_RE(self):
        re_code = """
                import java.util.Scanner;
                public class Solution {
                    public static void main(String[] args) {
                        Scanner sc=new Scanner(System.in);
                        int data[] = new int[3];

                        int a=sc.nextInt(),b=sc.nextInt();
                        System.out.println(a+b+data[4]);
                    }
                }
"""
        submitted_executor = get_executor(self.submission_lang, re_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 5000,
            "memory_limit": 262144,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])
        self.assertEqual(result['verdict'], VerdictResult.RE)

    def test_TLE(self):
        tle_code = """
import java.util.Scanner;
import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt(),b=sc.nextInt();
        ArrayList<Integer> arr = new ArrayList<Integer>();
        int t = 20000000;
        for (int i = 0; i < t; ++i) {
            arr.add(1);
            arr.remove(arr.size() - 1);
        }
        System.out.println(a+b);
    }
}
"""
        submitted_executor = get_executor(self.submission_lang, tle_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 100,
            "memory_limit": 262144,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])
        self.assertEqual(result['verdict'], VerdictResult.TLE)

    @unittest.skip("java MLE unsupported now")
    def test_MLE(self):
        mle_code = """
                       import java.util.Scanner;
                       public class Solution {
                           public static void main(String[] args) {
                               Scanner sc=new Scanner(System.in);
                               int data[] = new int[20000000];

                               int a=sc.nextInt(),b=sc.nextInt();
                               System.out.println(a+b+data[4]);
                           }
                       }
"""
        submitted_executor = get_executor(self.submission_lang, mle_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 5000,
            "memory_limit": 262144,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])
        self.assertEqual(result['verdict'], VerdictResult.MLE)

    @unittest.skip('java runs so slow that takes too much time to hit OLE')
    def test_OLE(self):
        ole_code = f"""
                       import java.util.Scanner;
                       public class Solution {{
                           public static void main(String[] args) {{
                               Scanner sc=new Scanner(System.in);
                               int a=sc.nextInt(),b=sc.nextInt();
                               int t = 729145;
                               for (int i = 0; i < t; ++i) {{
                                 System.out.println("{'A' * 100}");
                               }}

                           }}
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
        self.assertEqual(result['verdict'], VerdictResult.OLE)

    def test_class_name(self):
        ac_code = """
        import java.util.Scanner;
        public class Fuck {
            public static void main(String[] args) {
                Scanner sc=new Scanner(System.in);
                int a=sc.nextInt(),b=sc.nextInt();
                System.out.println(a+b);
            }
        }
        """
        submitted_executor = get_executor(self.submission_lang, ac_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 5000,
            "memory_limit": 262144,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])
        self.assertEqual(result['verdict'], VerdictResult.AC)
        pass

    def tearDown(self) -> None:
        shutil.rmtree(self.submission_dir, ignore_errors=True)
