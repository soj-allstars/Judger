import lorun
from utils import create_file_to_write
from consts import VerdictResult


class BaseExecutor:
    def __init__(self, code, exe_dir):
        self.code = code
        self.exe_dir = exe_dir
        self.exe_args = None
        self.init()

    def init(self):
        raise NotImplementedError

    def execute(self, input_path, output_path, log_path, time_limit, memory_limit):
        input_file = open(input_path, 'r') if input_path else None
        output_file = create_file_to_write(output_path) if output_path else None
        log_file = create_file_to_write(log_path) if log_path else None

        result = {
            'result': VerdictResult.SE,
            'timeused': 0,
            'memoryused': 0,
            'desc': "lorun exited unexpectedly"
        }
        try:
            run_cfg = {
                'args': self.exe_args,
                'fd_in': input_file.fileno() if input_file else 0,
                'fd_out': output_file.fileno() if output_file else 0,
                'fd_err': log_file.fileno() if log_path else 0,
                'timelimit': time_limit,  # in MS
                'memorylimit': memory_limit,  # in KB
            }
            result = lorun.run(run_cfg)
        except SystemError:
            return result
        finally:
            self.get_additional_info(result, output_path, log_path)
            if input_file:
                input_file.close()
            if output_file:
                output_file.close()
            if log_file:
                log_file.close()
            # do some cleanups in subclasses if necessary
            self.cleanup()

        return result

    def get_additional_info(self, result, output_path, log_path):
        # get different infos in subclasses if necessary
        if not log_path:
            return
        with open(log_path, 'r') as f:
            result['desc'] = f.read()

    def cleanup(self):
        pass
