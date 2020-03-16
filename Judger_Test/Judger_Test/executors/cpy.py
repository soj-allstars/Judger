from executors.python import PythonExecutor


class CpyExecutor(PythonExecutor):
    lang = 'CPY'
    interpreter = "python"
    magic = 'cpython-38.opt-1'
