import pytest
from instructions.arithmetic import exec_arithmetic, exec_unary


@pytest.mark.parametrize("instr, a, b, expected", [
    ("ADD", 3, 5, 8),
    ("SUB", 10, 4, 6),
    ("MUL", 2, 3, 6),
    ("DIV", 8, 2, 4),
    ("MOD", 10, 3, 1),
])
def test_exec_arithmetic(instr, a, b, expected):
    stack = [a, b]
    exec_arithmetic(instr, stack)
    assert stack[-1] == expected


def test_exec_unary():
    stack = [5]
    exec_unary("NEG", stack)
    assert stack[-1] == -5
