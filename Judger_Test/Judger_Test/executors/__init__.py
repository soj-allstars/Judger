from executors.cpp import CppExecutor
from executors.cpy import CpyExecutor

_lang_executor_map = {
    "CPP": CppExecutor,
    "CPY": CpyExecutor
}


def get_executor(lang, code, exe_dir):
    return _lang_executor_map[lang](code, exe_dir)
