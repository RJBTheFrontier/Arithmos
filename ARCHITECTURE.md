
# Arithmos — Architecture

## 1. Overview

Arithmos is a modular arithmetic interpreter written in Python.

Its primary goal is to interpret and evaluate mathematical expressions through a custom-built language processing pipeline.

Unlike approaches that rely on Python's built-in `eval()`, Arithmos is designed to implement its own lexer, parser, abstract syntax tree (AST), and evaluator.

## 2. System Architecture

Arithmos follows a modular architecture in which each component has a distinct responsibility.

The planned interpretation pipeline is:

```text
User Input
    |
    v
    REPL
    |
    v
   Lexer
    |
    v
  Parser
    |
    v
  Custom AST
    |
    v
 Evaluator
    |
    v
   Result
```

### 2.1 Main Application (`main.py`)

The application's entry point.

Responsibilities:
- Initialize the application.
- Start the REPL.

### 2.2 Read-Eval-Print Loop (`repl.py`)

Manages interaction between the user and the interpreter.

Responsibilities:
- Read user input.
- Pass expressions into the interpretation pipeline.
- Display evaluation results.
- Handle exit commands and user-facing errors.

### 2.3 Token System (`tokens.py`)

Defines the structure and classification of tokens.

Components:
- `TokenType`: An enumeration of supported token categories.
- `Token`: An immutable dataclass containing token type, value, and source position.

### 2.4 Lexer (`lexer.py`)

Converts raw source text into a sequence of tokens.

Responsibilities:
- Recognize numeric literals and operators.
- Handle multi-character operators using lookahead.
- Skip irrelevant whitespace.
- Track character positions.
- Detect invalid characters and malformed numeric literals.

### 2.5 Parser (`parser.py`)

Transforms the token sequence into a structured representation of the expression.

Responsibilities:
- Enforce mathematical operator precedence.
- Recognize unary and binary operators.
- Handle parentheses.
- Detect syntactically invalid expressions.

### 2.6 AST Nodes (`nodes.py`)

Defines the custom Abstract Syntax Tree node classes.

These nodes represent the grammatical structure of mathematical expressions.

### 2.7 Evaluator (`evaluator.py`)

Traverses the AST and computes the resulting numerical value.

Responsibilities:
- Evaluate arithmetic operations.
- Handle mathematical errors.
- Return computed results.

## 3. Design Principles

### Modularity
Each component has a clearly defined responsibility.

### Separation of Concerns
Lexical analysis, parsing, evaluation, and user interaction remain independent.

### Explicit Evaluation
Only explicitly supported syntax and operations should be evaluated.

### Error Handling
Errors should be detected and reported at the appropriate stage of the pipeline.

### Extensibility
The architecture should allow future support for variables, assignments, and built-in mathematical functions.

## 4. Development Roadmap

| Version | Milestone |
|---|---|
| v0.1 | Basic arithmetic calculator |
| v0.2 | Lexer and tokenization |
| v0.3 | Parser and grammar |
| v0.4 | Custom AST and evaluator |
| v0.5 | Parentheses, precedence, and unary operators |
| v0.6 | Variables and assignments |
| v0.7 | Built-in mathematical functions |
| v1.0 | Complete initial interpreter |

## 5. Project Structure

```text
Arithmos/
├── src/
│   └── arithmos/
│       ├── __init__.py
│       ├── main.py
│       ├── repl.py
│       ├── tokens.py
│       ├── lexer.py
│       ├── parser.py
│       ├── nodes.py
│       └── evaluator.py
├── experiments/
│   └── ast_prototype.py
├── tests/
├── README.md
├── ARCHITECTURE.md
├── LICENSE
└── .gitignore
```

---

*This document describes the intended architecture. It will be updated as implementation decisions evolve.*
