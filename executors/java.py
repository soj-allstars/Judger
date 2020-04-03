from executors.base_executor import BaseExecutor
import lorun
from utils import create_file_to_write
from consts import VerdictResult
from exceptions import ExecutorInitException


class JavaExecutor(BaseExecutor):
    lang = 'JAVA'

    def init(self):
        name = 'Solution'
        code_path = f'{self.exe_dir}/{name}.java'
        code_file = create_file_to_write(code_path)
        code_file.write(self.code)
        code_file.close()

        log_path = f'{self.exe_dir}/compile.log'
        self.exe_args = ['java', '-classpath', self.exe_dir, name]  # overridden in `execute` method

        with open(log_path, 'w') as log_file:
            run_cfg = self.get_run_cfg(
                ['javac', code_path],
                0,
                0,
                log_file.fileno(),
            )
            result = lorun.run(run_cfg)

        if result['result'] != VerdictResult.AC:
            with open(log_path, 'r') as log_file:
                raise ExecutorInitException(log_file.read())

    def execute(self, input_path, output_path, log_path, time_limit, memory_limit, trace=False):
        # TODO Since JVM need up to 1GB memory to setup (this appears to be a bug, see the link below),
        # https://stackoverflow.com/questions/33793620/java-what-determines-the-maximum-max-heap-size-possible-in-a-linux-machine
        # and obviously we cannot set the memory limit to 1GB,
        # so we use JVM (-Xmx) to limit the memory use of the user program.
        #
        # Actually JVM can be a good sandbox through policy:
        # https://docs.oracle.com/javase/8/docs/technotes/guides/security/PolicyFiles.html
        self.exe_args = ['java', '-classpath', self.exe_dir, '-Xss1M', f'-Xmx{memory_limit}K', 'Solution']
        return super().execute(input_path, output_path, log_path, time_limit, -1, trace)

    def get_additional_info(self, result, output_path, log_path):
        super().get_additional_info(result, output_path, log_path)
        if not log_path:
            return

        # Get the first line of log.
        with open(log_path, 'r') as f:
            lines = f.readlines()
            result['desc'] = result.get('desc', '') + (lines[0] if lines else '')
