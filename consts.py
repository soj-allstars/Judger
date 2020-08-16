from enum import IntEnum, unique


@unique
class VerdictResult(IntEnum):
    AC = 0  # Accepted
    PE = 1  # Presentation Error
    TLE = 2  # Time Limit Exceeded
    MLE = 3  # Memory Limit Exceeded
    WA = 4  # Wrong Answer
    RE = 5  # Runtime Error
    OLE = 6  # Output Limit Exceeded
    CE = 7  # Compile Error
    SE = 8  # System Error


RESULT_STR = [
    'Accepted',
    'Presentation Error',
    'Time Limit Exceeded',
    'Memory Limit Exceeded',
    'Wrong Answer',
    'Runtime Error',
    'Output Limit Exceeded',
    'Compile Error',
    'System Error'
]


NOBODY_UID = 65534
