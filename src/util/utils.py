from enum import Enum


class TokenType(Enum):
    # Single-character tokens.
    LEFT_PAREN = 1
    RIGHT_PAREN = 2
    LEFT_BRACE = 3
    RIGHT_BRACE = 4
    COMMA = 5
    DOT = 6
    MINUS = 7
    PLUS = 8
    SEMICOLON = 9
    SLASH = 10
    STAR = 11

    # One or two character tokens.
    BANG = 12
    BANG_EQUAL = 13
    EQUAL = 14
    EQUAL_EQUAL = 15
    GREATER = 16
    GREATER_EQUAL = 17
    LESS = 18
    LESS_EQUAL = 19

    # Literals.
    IDENTIFIER = 20
    STRING = 21
    NUMBER = 22

    # Keywords.
    AND = 23
    CLASS = 24
    ELSE = 25
    FALSE = 26
    FUN = 27
    FOR = 28
    IF = 29
    NULL = 30
    OR = 31
    PRINT = 32
    RETURN = 33
    SUPER = 34
    THIS = 35
    TRUE = 36
    VAR = 37
    WHILE = 38
    ELSE_IF = 39
    BEGIN = 40
    END = 41
    EOF = 42

class Token():
    def __init__(self, tokenType: TokenType, lexeme: str, literal: str, line: str) -> None:
        self.tokenType = tokenType
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
    
