from executors.python import PythonExecutor


class PypyExecutor(PythonExecutor):
    lang = 'PYPY'
    interpreter = "pypy3"
    magic = 'pypy36.opt-1'
