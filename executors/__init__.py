from executors.gxx import GxxExecutor
from executors.cpy import CpyExecutor
from executors.gcc import GccExecutor
from executors.java import JavaExecutor
from executors.pypy import PypyExecutor

_lang_executor_map = {
    "GXX": GxxExecutor,
    "CPY": CpyExecutor,
    "GCC": GccExecutor,
    "JAVA": JavaExecutor,
    "PYPY": PypyExecutor,
}


def get_executor(lang, code, exe_dir):
    return _lang_executor_map[lang](code, exe_dir)
