import lorun
from utils import create_file_to_write
from consts import VerdictResult
from conf import run_cfgs as cfgs
import os


class BaseExecutor:
    lang = None

    def __init__(self, code, exe_dir):
        self.code = code
        self.exe_dir = exe_dir
        self.exe_args = None
        self.init()

    def init(self):
        raise NotImplementedError

    def execute(self, input_path, output_path, log_path, time_limit, memory_limit, trace=False):
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
            run_cfg = self.get_run_cfg(
                self.exe_args,
                input_file.fileno() if input_file else 0,
                output_file.fileno() if output_file else 0,
                log_file.fileno() if log_path else 0,
                time_limit,
                memory_limit,
                trace=trace,
            )
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
            self.cleanup(log_path)

        return result

    def get_additional_info(self, result, output_path, log_path):
        # get more info in subclasses if necessary
        info = []
        if "re_call" in result:
            info.append(f"re_call: {result['re_call']}")
        if "re_signum" in result:
            info.append(f"re_signum: {result['re_signum']}")
        if "re_file" in result:
            info.append(f"re_file: {result['re_file']}\nre_file_flag: {result['re_file_flag']}")
        result['desc'] = "\n".join(info)

    def cleanup(self, log_path):
        if log_path:
            if os.path.getsize(log_path) == 0:
                os.remove(log_path)

    def get_run_cfg(self, args, fd_in, fd_out, fd_err, time_limit=None, memory_limit=None, trace=False):
        cfg = cfgs[self.lang]
        res = {
            'args': args,
            'fd_in': fd_in,
            'fd_out': fd_out,
            'fd_err': fd_err,
            'timelimit': time_limit,  # in MS
            'memorylimit': memory_limit,  # in KB
        }
        # If no *_limit is set, which means the cfg is for compilation, read limits from config file.
        if not time_limit:
            res['timelimit'] = cfg['compile_time_limit']
        if not memory_limit:
            res['memorylimit'] = cfg['compile_memory_limit']
        if trace:
            res.update({'trace': True, 'calls': cfg['allowed_calls'], 'files': cfg['allowed_files']})
        return res
