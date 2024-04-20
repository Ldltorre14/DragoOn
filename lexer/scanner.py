import sys
sys.path.append('util/utils')
from util.utils import TokenType, Token


class Scanner():
    def __init__(self, sourceCode: str) -> None:
        self.tokens = []
        self.sourceCode = sourceCode
        self.start = 0
        self.current = 0
        self.line = 0
    
    #Compare is the current char is >= to the source code
    def isAtEnd(self):
        return self.current >= len(self.sourceCode)  
    
    #Consume the next character in the source code and returns it
    def advance(self):
        currChar = self.sourceCode[self.current]
        self.current += 1
        return currChar

    #Alternative Advance method which only advances current if it matches and expected char
    def match(self, expectedChar):
        if self.isAtEnd():
            return False
        elif self.sourceCode[self.current] != expectedChar:
            return False
        self.current += 1
        return True
        
    def addToken(self, type: TokenType, literal = None):
        text = self.sourceCode[self.start : self.current]
        self.tokens.append(Token(type, text, literal, self.line))
    
    def scan(self):
        #Keep scanning tokkens until it reaches the end of the source code
        while(not self.isAtEnd()):
            self.start = self.current
            self.scanToken()
        #Appends an EOF Token for readability    
        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        
    def scanToken(self):
        char = self.advance()
        if char == '(': 
            self.addToken(TokenType.LEFT_PAREN)
            print(char)
        elif char == ')':
            self.addToken(TokenType.RIGHT_PAREN)
            print(char)
        elif char == '{':
            self.addToken(TokenType.LEFT_BRACE)
            print(char)
        elif char == '}':
            self.addToken(TokenType.RIGHT_BRACE)
            print(char)
        elif char == ',':
            self.addToken(TokenType.COMMA)
            print(char)
        elif char == '.':
            self.addToken(TokenType.DOT)
            print(char)
        elif char == ';':
            self.addToken(TokenType.SEMICOLON)
            print(char)
        elif char == '-':
            self.addToken(TokenType.MINUS)
            print(char)
        elif char == '+':
            self.addToken(TokenType.PLUS)
            print(char)
        elif char == '*':
            self.addToken(TokenType.STAR)
            print(char)
        elif char == '!':
            self.addToken(TokenType.BANG_EQUAL if self.match('=') else TokenType.BANG)
            print(char)
        elif char == '=':
            self.addToken(TokenType.EQUAL_EQUAL if self.match('=') else TokenType.EQUAL)
            print(char)
        elif char == '<':
            self.addToken(TokenType.LESS_EQUAL if self.match('=') else TokenType.LESS)
            print(char)
        elif char == '>':
            self.addToken(TokenType.GREATER_EQUAL if self.match('=') else TokenType.GREATER)
            print(char)
        else:
            print(f"Unexpected Character{char}" + " at line ", self.line)
        
        