from instructions.variables import exec_variable
from vm_state import VMState


def test_variable_store():
    state = VMState()
    state.stack.append(42)  # Value to store
    exec_variable("STORE", ["x"], state.stack, state.memory)
    assert "x" in state.memory
    assert state.memory["x"] == 42
    assert len(state.stack) == 0  # Stack should be empty after storing


def test_variable_load():
    state = VMState()
    state.memory["x"] = 42  # Preload memory with a value
    exec_variable("LOAD", ["x"], state.stack, state.memory)
    assert state.stack[-1] == 42  # Value should be pushed to the stack
