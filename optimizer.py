def try_fold(op, a, b):
    if op == "ADD":
        return a + b
    elif op == "SUB":
        return a - b
    elif op == "MUL":
        return a * b
    elif op == "DIV":
        return a // b
    elif op == "MOD":
        return a % b
    return None


def apply_const_folding(bytecode_lines):
    optimized = []
    i = 0
    while i < len(bytecode_lines):
        line = bytecode_lines[i].strip()

        if (i + 2 < len(bytecode_lines) and
                line.startswith("PUSH") and
                bytecode_lines[i + 1].strip().startswith("PUSH") and
                bytecode_lines[i + 2].strip() in ["ADD", "SUB", "MUL", "DIV", "MOD"]):

            a = line.split()[1]
            b = bytecode_lines[i + 1].strip().split()[1]
            op = bytecode_lines[i + 2].strip()
            try:
                folded = try_fold(op, int(a), int(b))
                print(f"Successfully folded: {a} {op} {b} = {folded}")
                optimized.append(f"PUSH {folded}")
                i += 3
                continue
            except Exception:
                pass

        optimized.append(line)
        i += 1
    return optimized
