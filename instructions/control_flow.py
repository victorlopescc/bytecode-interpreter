def resolve_target(arg, labels):
    if arg in labels:
        return labels[arg]
    try:
        address = int(arg)
        line_index = address // 4  # Cada instrução ocupa 4 bytes
        return line_index
    except ValueError:
        raise KeyError(f"Unknown label or invalid address: '{arg}'")


def exec_jump(instr, args, stack, labels, pc):
    target = resolve_target(args[0], labels)

    if instr == "JMP":
        return target
    elif instr == "JZ":
        val = stack.pop()
        # Se o valor for zero, salta para o destino
        return target if val == 0 else pc + 1
    elif instr == "JNZ":
        val = stack.pop()
        # Se o valor não for zero, salta para o destino
        return target if val != 0 else pc + 1

    return pc + 1
