from instructions.functions_io import exec_io, exec_function


def test_exec_io_print(capsys):
    stack = [42]
    exec_io("PRINT", stack)
    captured = capsys.readouterr()
    assert captured.out.strip() == "42"


def test_exec_io_read(monkeypatch):
    stack = []
    monkeypatch.setattr("builtins.input", lambda: "10")
    exec_io("READ", stack)
    assert stack[-1] == 10


def test_exec_function_ret():
    call_stack = [5, 10]
    pc = exec_function("RET", 0, call_stack)
    assert pc == 10
    assert call_stack == [5]
