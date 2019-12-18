import os
from checkers.cf_checker import CFChecker



def get_checker(checker_type):
    if checker_type != 'same' and checker_type != 'special_judge':
        return CFChecker(checker_type)

    raise NotImplementedError
