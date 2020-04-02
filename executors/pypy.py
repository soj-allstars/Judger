from executors.python import PythonExecutor


class PypyExecutor(PythonExecutor):
    lang = 'PYPY'
    interpreter = "pypy3"
    magic = 'pypy3-70.opt-1'
