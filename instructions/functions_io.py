def exec_io(instr, stack):
    if instr == "PRINT":
        print(stack[-1])
    elif instr == "READ":
        val = int(input())
        stack.append(val)


def exec_function(instr, pc, call_stack):
    if instr == "RET":
        return call_stack.pop()
    return pc + 1
