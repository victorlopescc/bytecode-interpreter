def exec_variable(instr, args, stack, memory):
    if instr == "STORE":
        memory[args[0]] = stack.pop()
    elif instr == "LOAD":
        stack.append(memory.get(args[0], 0))
