import logging
import tkinter as tk
from tkinter import filedialog
from vm_state import VMState
from utils import preprocess_labels
from instructions.arithmetic import exec_arithmetic, exec_unary
from instructions.variables import exec_variable
from instructions.control_flow import exec_jump, resolve_target
from instructions.comparison import exec_comparison
from instructions.functions_io import exec_io, exec_function
from optimizer import apply_const_folding

logging.basicConfig(level=logging.INFO, format="%(message)s")


def execute_instruction(instr, args, state):
    if instr == "PUSH":
        state.stack.append(int(args[0]))
    elif instr == "POP":
        state.stack.pop()
    elif instr in ["ADD", "SUB", "MUL", "DIV", "MOD"]:
        exec_arithmetic(instr, state.stack)
    elif instr in ["EQ", "NEQ", "LT", "GT", "LE", "GE"]:
        exec_comparison(instr, state.stack)
    elif instr == "NEG":
        exec_unary(instr, state.stack)
    elif instr in ["STORE", "LOAD"]:
        exec_variable(instr, args, state.stack, state.memory)
    elif instr in ["JMP", "JZ", "JNZ"]:
        state.pc = exec_jump(instr, args, state.stack, state.labels, state.pc)
        return True
    elif instr in ["CALL"]:
        state.call_stack.append(state.pc + 1)
        target = resolve_target(args[0], state.labels)
        state.pc = target
        return True
    elif instr in ["RET"]:
        state.pc = exec_function(instr, state.pc, state.call_stack)
        return True
    elif instr in ["PRINT", "READ"]:
        exec_io(instr, state.stack)
    elif instr == "HALT":
        return False
    return None


def interpret(bytecode_lines):
    state = VMState()
    bytecode_lines = apply_const_folding(bytecode_lines)
    state.labels = preprocess_labels(bytecode_lines)

    while state.pc < len(bytecode_lines):
        line = bytecode_lines[state.pc].strip()
        if not line or line.endswith(":"):
            state.pc += 1
            continue

        parts = line.split()
        instr = parts[0]
        args = parts[1:]

        logging.info(f"PC: {state.pc}, Instruction: {instr}, Stack: {state.stack}")
        result = execute_instruction(instr, args, state)
        if result is False:
            break
        if result is not True:
            state.pc += 1


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    input_file = filedialog.askopenfilename(title="Select Bytecode File", filetypes=[("Text Files", "*.txt")])

    if not input_file:
        print("No file selected. Exiting.")
        exit(1)

    with open(input_file, "r", encoding="utf-8") as f:
        bytecode = f.readlines()

    interpret(bytecode)
