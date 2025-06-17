def exec_comparison(instr, stack):
    b = stack.pop()
    a = stack.pop()
    if instr == "EQ":
        stack.append(int(a == b))
    elif instr == "NEQ":
        stack.append(int(a != b))
    elif instr == "LT":
        stack.append(int(a < b))
    elif instr == "GT":
        stack.append(int(a > b))
    elif instr == "LE":
        stack.append(int(a <= b))
    elif instr == "GE":
        stack.append(int(a >= b))
