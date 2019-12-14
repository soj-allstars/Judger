import lorun


class BaseExecutor:
    def __init__(self, code):
        self.code = code
        self.exe_args = None
        self.init()

    def init(self):
        raise NotImplementedError

    def execute(self, input_path, output_path, time_limit, memory_limit):
        input_file = open(input_path, 'r')
        output_file = open(output_path, 'w')

        run_cfg = {
            'args': self.exe_args,
            'fd_in': input_file.fileno(),
            'fd_out': output_file.fileno(),
            'timelimit': time_limit,  # in MS
            'memorylimit': memory_limit,  # in KB
        }
        result = lorun.run(run_cfg)
        input_file.close()
        output_file.close()

        self.post_execution()
        return result

    def post_execution(self):
        pass
