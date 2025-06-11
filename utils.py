def preprocess_labels(bytecode_lines):
    labels = {}
    for idx, line in enumerate(bytecode_lines):
        line = line.strip()
        if line.endswith(":"):
            label = line[:-1].strip()
            labels[label] = idx
    return labels
