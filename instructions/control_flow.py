def resolve_target(arg, labels):
    if arg in labels:
        return labels[arg]
    raise KeyError(f"Unknown label: {arg}")


def exec_jump(instr, args, stack, labels, pc):
    target = resolve_target(args[0], labels)

    if instr == "JMP":
        return target
    elif instr == "JZ":
        val = stack.pop()
        return target if val == 0 else pc + 1
    elif instr == "JNZ":
        val = stack.pop()
        return target if val != 0 else pc + 1

    return pc + 1
