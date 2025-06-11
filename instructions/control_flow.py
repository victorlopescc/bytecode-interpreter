def resolve_target(arg, labels):
    if arg in labels:
        return labels[arg]
    try:
        address = int(arg)
        line_index = address // 4  # ← regra do professor
        return line_index
    except ValueError:
        raise KeyError(f"Label desconhecida ou endereço inválido: {arg}")


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
