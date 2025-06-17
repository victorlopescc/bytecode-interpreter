def preprocess_labels(bytecode_lines):
    """
    Preprocesses bytecode lines to extract labels and their corresponding line numbers.
    :param bytecode_lines: List of strings representing bytecode lines.
    :return: A dictionary mapping label names to their line numbers.
    """
    labels = {}
    for idx, line in enumerate(bytecode_lines):
        line = line.strip()
        if line.endswith(":"):
            label = line[:-1].strip()
            labels[label] = idx
    return labels
