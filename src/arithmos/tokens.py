from dataclasses import dataclass
from enum import Enum, auto
from typing import Any


class TokenType(Enum):
    # Numeric literals
    NUMBER = auto()

    # Math operators
    PLUS = auto()  # +
    MINUS = auto()  # -
    MULT = auto()  # *
    DIV = auto()  # /
    FLOOR_DIV = auto()  # //
    MOD = auto()  # %
    POW = auto()  # ^ or **

    LPAREN = auto()  # (
    RPAREN = auto()  # )

    EOF = auto()  # End of File/End of Input


@dataclass(frozen=True)
class Token:
    type: TokenType
    value: Any
    position: int

    def __repr__(self) -> str:
        """Custom clean string representation for easier debugging and printing."""
        # Handles strings cleanly while keeping numbers looking like numbers
        val_repr = f"'{self.value}'" if isinstance(self.value, str) else self.value
        return f"Token({self.type}, {val_repr}, {self.position})"


# ==========================================
# Acceptance Tests / Verification Block
# ==========================================
if __name__ == "__main__":
    print("--- Running Acceptance Tests ---")

    # Test 1: Number Token
    t1 = Token(TokenType.NUMBER, 12, 0)
    print(t1)

    # Test 2: Operator Token
    t2 = Token(TokenType.PLUS, "+", 3)
    print(t2)

    # Test 3: EOF Token
    t3 = Token(TokenType.EOF, None, 4)
    print(t3)

    print("\n--- Structural Attribute Verification ---")
    assert t1.type == TokenType.NUMBER
    assert t1.value == 12
    assert t1.position == 0
    print("All assertions passed cleanly! Data properties match exactly.")
