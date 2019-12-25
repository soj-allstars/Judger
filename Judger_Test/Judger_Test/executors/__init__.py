from executors.cpp import CppExecutor
from executors.cpy import CpyExecutor

_lang_executor_map = {
    "G++": CppExecutor,
    "CPY": CpyExecutor
	"GCC": GccExecutor
}


def get_executor(lang, code, exe_dir):
    return _lang_executor_map[lang](code, exe_dir)
