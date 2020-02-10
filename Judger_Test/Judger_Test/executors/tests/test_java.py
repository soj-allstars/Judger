import unittest
import conf
from judge_jobs import do_judge
from executors import get_executor
from consts import VerdictResult
import shutil
import exceptions


class TestJava(unittest.TestCase):
    submission_lang = "JAVA"
    submission_dir = f'problems/1/test'

    def test_AC(self):
        self.submission_dir = f'problems/1/test'
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
            "memory_limit": 1500000,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])
        self.assertEqual(result['verdict'], VerdictResult.AC)

    def test_WA(self):
        self.submission_dir = f'problems/1/test'
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
            "memory_limit": 1500000,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])
        self.assertEqual(result['verdict'], VerdictResult.WA)

    def test_CE(self):
        self.submission_dir = f'problems/1/test'
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
        self.submission_dir = f'problems/1/test'
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
            "memory_limit": 1500000,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])
        self.assertEqual(result['verdict'], VerdictResult.RE)

    def test_TLE(self):
        self.submission_dir = f'problems/1/test'
        tle_code = """
                import java.util.Scanner;
                public class Solution {
                    public static void main(String[] args) {
                        Scanner sc=new Scanner(System.in);
                        int a=sc.nextInt(),b=sc.nextInt();                        
                        int t = 2000000000;
                        while(a < t){
                         a = a + b;
                        }
                        System.out.println(a+b);
                    }
                }
                """
        submitted_executor = get_executor(self.submission_lang, tle_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 1000,
            "memory_limit": 1500000,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])
        self.assertEqual(result['verdict'], VerdictResult.TLE)

    @unittest.skip("MLE can't test")
    def test_MLE(self):
        self.submission_dir = f'problems/1/test'
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
            "memory_limit": 1200000,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])
        self.assertEqual(result['verdict'], VerdictResult.MLE)

    def test_OLE(self):
        self.submission_dir = f'problems/1/test'
        ole_code = """
                       import java.util.Scanner;
                       public class Solution {
                           public static void main(String[] args) {
                               Scanner sc=new Scanner(System.in);
                               int a=sc.nextInt(),b=sc.nextInt();
                               int t = 100000000;
                               int t1 = 1;
                               while(t1 < t){
                                 t1 = t1 + 1;
                                 System.out.println(a+b);
                                }

                           }
                       }
                       """
        submitted_executor = get_executor(self.submission_lang, ole_code, f'{self.submission_dir}/submitted')
        result = do_judge({
            "submit_id": 1,
            "problem_id": 1,
            "time_limit": 5000,
            "memory_limit": 1200000,
            "checker_type": "icmp",
        }, self.submission_dir, submitted_executor)
        print(result['desc'])
        self.assertEqual(result['verdict'], VerdictResult.OLE)

    def tearDown(self) -> None:
        shutil.rmtree(self.submission_dir, ignore_errors=True)