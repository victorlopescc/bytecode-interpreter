def exec_arithmetic(instr, stack):
    b = stack.pop()
    a = stack.pop()
    if instr == "ADD":
        stack.append(a + b)
    elif instr == "SUB":
        stack.append(a - b)
    elif instr == "MUL":
        stack.append(a * b)
    elif instr == "DIV":
        try:
            stack.append(a // b)
        except ZeroDivisionError:
            print("Zero Division Detected, 0 is added in the stack.")
            stack.append(0)
    elif instr == "MOD":
        stack.append(a % b)


def exec_unary(instr, stack):
    if instr == "NEG":
        val = stack.pop()
        stack.append(-val)
