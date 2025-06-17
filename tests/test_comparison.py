import pytest
from instructions.comparison import exec_comparison


@pytest.mark.parametrize("instr, a, b, expected", [
    ("EQ", 5, 5, 1),
    ("NEQ", 5, 3, 1),
    ("LT", 3, 5, 1),
    ("GT", 5, 3, 1),
    ("LE", 3, 3, 1),
    ("GE", 5, 5, 1),
])
def test_exec_comparison(instr, a, b, expected):
    stack = [a, b]
    exec_comparison(instr, stack)
    assert stack[-1] == expected
