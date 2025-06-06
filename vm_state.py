class VMState:
    def __init__(self):
        self.stack = []
        self.memory = {}
        self.labels = {}
        self.pc = 0
        self.call_stack = []
