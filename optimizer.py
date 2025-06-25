import logging


def try_fold(op, a, b):
    """
    Attempt to fold a binary operation on two constants.
    :param op: The operation to perform, one of "ADD", "SUB", "MUL", "DIV", "MOD".
    :param a: Numeric constant a.
    :param b: Numeric constant b.
    :return: The result of the operation if successful, otherwise None.
    """
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
    """
    Apply constant folding optimization to a list of bytecode lines.
    :param bytecode_lines: List of bytecode lines as strings.
    :return: List of optimized bytecode lines.
    """
    optimized = []  # Lista de linhas otimizadas
    i = 0
    while i < len(bytecode_lines):
        line = bytecode_lines[i].strip()

        # Verifica se a linha é uma instrução PUSH seguida por outra PUSH e uma operação binária
        if (i + 2 < len(bytecode_lines) and
                line.startswith("PUSH") and
                bytecode_lines[i + 1].strip().startswith("PUSH") and
                bytecode_lines[i + 2].strip() in ["ADD", "SUB", "MUL", "DIV", "MOD"]):

            a = line.split()[1]
            b = bytecode_lines[i + 1].strip().split()[1]
            op = bytecode_lines[i + 2].strip()
            try:
                folded = try_fold(op, int(a), int(b))  # Tenta realizar a operação se ambos forem constantes
                print(f"Folding: {a} {op} {b} -> {folded}")
                optimized.append(f"PUSH {folded}")
                i += 3
                continue
            except ValueError:
                print(f"Failed to fold: {a} {op} {b}")

        optimized.append(line)
        i += 1
    return optimized
