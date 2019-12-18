from executors.cpp import CppExecutor


_lang_executor_map = {
    "CPP": CppExecutor
}


def get_executor(lang, code, exe_dir):
    return _lang_executor_map[lang](code, exe_dir)
