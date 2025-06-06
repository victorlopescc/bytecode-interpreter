# bytecode-interpreter

## Project Structure

bytecode_vm/
│
├── main.py                Entry point of the interpreter
├── vm_state.py            Defines the VM state: stack, memory, pc, labels and call stack.
│
├── instructions/          Contains instruction-specific modules
│   ├── arithmetic.py      Arithmetic instructions: ADD, SUB, MUL, DIV, MOD, NEG
│   ├── variables.py       Variable instructions: STORE, LOAD
│   ├── control_flow.py    Control flow: JMP, JZ, JNZ, HALT
│   ├── comparison.py      Comparisons: EQ, NEQ, LT, GT, LE, GE
│   └── functions_io.py    Functions and I/O: CALL, RET, PRINT, READ
│
├── optimizer.py           Optimizes bytecode using constant folding
├── utils.py               Utilities like parsing and labels
│
└──  inputs/               Directory for bytecode input files