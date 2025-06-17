from instructions.control_flow import resolve_target, exec_jump


def test_resolve_target_with_label():
    labels = {"start": 10}
    assert resolve_target("start", labels) == 10


def test_resolve_target_with_address():
    labels = {}
    assert resolve_target("8", labels) == 2


def test_exec_jump_jmp():
    labels = {"start": 10}
    pc = exec_jump("JMP", ["start"], [], labels, 0)
    assert pc == 10


def test_exec_jump_jz():
    stack = [0]
    labels = {"start": 10}
    pc = exec_jump("JZ", ["start"], stack, labels, 0)
    assert pc == 10


def test_exec_jump_jnz():
    stack = [1]
    labels = {"start": 10}
    pc = exec_jump("JNZ", ["start"], stack, labels, 0)
    assert pc == 10
