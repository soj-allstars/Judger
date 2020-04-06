from checkers.cf_checker import CFChecker


def get_checker(checker_type):
    if checker_type != 'same':
        return CFChecker(checker_type)

    raise NotImplementedError
