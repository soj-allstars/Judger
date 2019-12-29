from executors.gxx import GxxExecutor
from executors.cpy import CpyExecutor
from executors.gcc import GccExecutor
_lang_executor_map = {
    "GXX": GxxExecutor,
    "CPY": CpyExecutor,
    "GCC": GccExecutor
}


def get_executor(lang, code, exe_dir):
    return _lang_executor_map[lang](code, exe_dir)
