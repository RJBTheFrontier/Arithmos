from arithmos.tokens import Token, TokenType


def test_number_token():
    token = Token(TokenType.NUMBER, 12, 0)

    assert token.type == TokenType.NUMBER
    assert token.value == 12
    assert token.position == 0


def test_operator_token():
    token = Token(TokenType.PLUS, "+", 3)

    assert token.type == TokenType.PLUS
    assert token.value == "+"
    assert token.position == 3


def test_eof_token():
    token = Token(TokenType.EOF, None, 4)

    assert token.type == TokenType.EOF
    assert token.value is None
    assert token.position == 4
