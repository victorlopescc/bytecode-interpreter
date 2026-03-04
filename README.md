# Bytecode Interpreter 🧠

Interpretador de **bytecode** desenvolvido durante a disciplina de **Compiladores**.

O projeto simula o funcionamento de uma máquina virtual (VM), executando instruções a partir de arquivos de entrada contendo bytecode.

## 📌 Sobre o Projeto

O interpretador foi projetado para:

- Executar instruções baseadas em pilha (stack-based VM)
- Controlar fluxo de execução (saltos, chamadas de função, etc.)
- Manipular variáveis e memória
- Realizar operações aritméticas e comparações
- Executar entrada e saída (I/O)
- Aplicar otimizações simples como *constant folding*

## 🏗 Estrutura do Projeto
```
bytecode-interpreter/
│
├── main.py                Entry point of the interpreter
├── vm_state.py            Defines the VM state: stack, memory, pc, labels and call stack.
│
├── instructions/          Contains instruction-specific modules
│   ├── arithmetic.py      Arithmetic instructions: ADD, SUB, MUL, DIV, MOD, NEG
│   ├── variables.py       Variable instructions: STORE, LOAD
│   ├── control_flow.py    Control flow: JMP, JZ, JNZ, CALL, RET, HALT
│   ├── comparison.py      Comparisons: EQ, NEQ, LT, GT, LE, GE
│   └── functions_io.py    Functions and I/O: PRINT, READ
│
├── optimizer.py           Optimizes bytecode using constant folding
├── utils.py               Utilities like parsing and labels
│
└──  inputs/               Directory for bytecode input files
```

## ⚙️ Funcionalidades

- 🧮 Operações aritméticas
- 🔀 Controle de fluxo
- 📦 Manipulação de variáveis
- 🔁 Chamadas de função com call stack
- 📉 Otimização de bytecode
- 🖨 Entrada e saída

## 🎯 Objetivo

O principal objetivo foi compreender na prática:

- Funcionamento de uma máquina virtual
- Execução de bytecode
- Organização modular de instruções
- Aplicação de técnicas simples de otimização
