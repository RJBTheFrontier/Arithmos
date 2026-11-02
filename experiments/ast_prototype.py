import ast
import operator

# Map Abstract Syntax Tree nodes to safe Python operator functions
SUPPORTED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: lambda x: x,
}

# Safety thresholds to prevent CPU/Memory exhaustion attacks
MAX_EXPONENT = 1000
MAX_BASE_FOR_EXPONENT = 10**6


def calculate(expression: str):
    """Parses and securely evaluates an arithmetic expression string with structural guards.

    Supports: +, -, *, /, //, %, **, ^, parentheses, and negative numbers.
    """
    if not isinstance(expression, str):
        return "Error: Input must be a string expression."

    # 1. Standardize power operator symbol before parsing
    clean_expr = expression.replace("^", "**")

    try:
        # 2. Parse the string into an AST structure
        node = ast.parse(clean_expr, mode="eval").body
        result = _evaluate_node(node)

        # Final sanity check: Ensure the output is strictly numeric
        if not isinstance(result, (int, float)) or isinstance(result, bool):
            return "Error: Evaluation did not result in a valid number."

        return result

    except (SyntaxError, KeyError, TypeError, ValueError):
        # Gracefully handle malicious syntax, missing operators, or bad types
        return "Error: Invalid expression or unsupported operation."
    except ZeroDivisionError:
        return "Error: Division or modulo by zero is undefined."
    except OverflowError:
        return "Error: Resulting value is too large to compute (Overflow)."


def _evaluate_node(node):
    """Recursively traverses and evaluates approved syntax tree nodes with strict type and size validation."""

    # Task 1 & 4: Restrict constants exclusively to real numbers (int/float).
    # explicitly blocks strings, booleans, bytes, None, etc.
    if isinstance(node, ast.Constant):
        if type(node.value) in (int, float) and not isinstance(node.value, bool):
            return node.value
        raise TypeError("Non-numeric constants are strictly forbidden.")

    # Task 4: Explicitly handle binary operations and block any unmapped structures
    elif isinstance(node, ast.BinOp):
        op_type = type(node.op)

        if op_type not in SUPPORTED_OPERATORS:
            raise KeyError("Unsupported binary operator.")

        left_val = _evaluate_node(node.left)
        right_val = _evaluate_node(node.right)

        # Task 3: Catch division/modulo by zero early at the node level
        if op_type in (ast.Div, ast.FloorDiv, ast.Mod) and right_val == 0:
            raise ZeroDivisionError

        # Task 2: Prevent unreasonable exponentiation (DoS vectors like 9**9**9)
        if op_type == ast.Pow:
            if right_val > MAX_EXPONENT or (
                left_val > MAX_BASE_FOR_EXPONENT and right_val > 1
            ):
                raise ValueError("Exponentiation values exceed safety thresholds.")

        return SUPPORTED_OPERATORS[op_type](left_val, right_val)

    # Task 4: Explicitly handle unary operations (+/- signs)
    elif isinstance(node, ast.UnaryOp):
        op_type = type(node.op)

        if op_type not in SUPPORTED_OPERATORS:
            raise KeyError("Unsupported unary operator.")

        operand_val = _evaluate_node(node.operand)
        return SUPPORTED_OPERATORS[op_type](operand_val)

    # Task 4: Hard structural barrier against variables, lookups, strings, or code blocks
    else:
        raise TypeError("Unsupported or malicious AST node detected.")
