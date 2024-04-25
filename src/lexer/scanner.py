import sys
sys.path.append('src/util/utils')
from util.utils import Token, TokenType


class Scanner():
    def __init__(self, sourceCode: str) -> None:
        self.tokens = []
        self.keywords = {"and" : TokenType.AND,
                         "or" : TokenType.OR,
                         "true" : TokenType.TRUE,
                         "false" : TokenType.FALSE,
                         "if" : TokenType.IF,
                         "else if" : TokenType.ELSE_IF,
                         "for" : TokenType.FOR,
                         "while" : TokenType.WHILE,
                         "this" : TokenType.THIS,
                         "var" : TokenType.VAR,
                         "class" : TokenType.CLASS,
                         "return" : TokenType.RETURN,
                         "print" : TokenType.PRINT}
        self.sourceCode = sourceCode
        self.start = 0
        self.current = 0
        self.line = 0
    
    #Simple method for printing the scanned Tokens
    def printTokens(self):
        for token in self.tokens:
            print(f"Token\n TYPE:{token.tokenType}\t LEXEME:{token.lexeme}\t LITERAL:{token.literal}\t LINE:{token.line}")
    
    #Compare is the current char is >= to the source code
    def isAtEnd(self):
        return self.current >= len(self.sourceCode)  
    
    #Consume the next character in the source code and returns it
    def advance(self):
        currChar = self.sourceCode[self.current]
        self.current += 1
        return currChar
    
    #We return the current char without consuming it (null string if end)
    def peek(self):
        if self.isAtEnd():
            return '\0'
        return self.sourceCode[self.current]

    #Alternative Peek for reeding the next char without consuming it
    def peekNext(self):
        if self.current + 1 >= len(self.sourceCode):
            return '\0'
        return self.sourceCode[self.current + 1]
    
    #method for reading string literals 
    def readString(self):
        #After finding the string in the 'scan' method, we keep reading until we find the second
        #closing '"'
        while self.peek != '"' and not self.isAtEnd():
            if self.peek() == '\n':
                self.line += 1
            self.advance()
            
        #If we reach the end of the source code before getting the second '"" we throw an
        #unterminated string error
        if self.isAtEnd():
            print(f"ERROR: Unterminated string at line {self.line} in col {self.current}")
        
        #For the closing "
        self.advance()
        
        #We trim the quotes from the string value
        value = self.sourceCode[self.start+1 : self.current-1]
        self.addToken(TokenType.STRING, value)
    
    #Method for reading a string of numbers    
    def readNumber(self):
        #We keep reading the string until we find '\0'
        while self.isDigit(self.peek()):
            self.advance()
        #if we read a point and the next char is a digit, then we have a decimal number
        if self.peek() == '.' and self.isDigit(self.peekNext()):
            self.advance()
            #After passing the point we read the decimals
            while self.isDigit(self.peek()):
                self.advance()
                
        self.addToken(TokenType.NUMBER,float(self.sourceCode[self.start : self.current]))

    #Alternative Advance method which only advances current if it matches and expected char
    def match(self, expectedChar):
        if self.isAtEnd():
            return False
        elif self.sourceCode[self.current] != expectedChar:
            return False
        self.current += 1
        return True
    
    #Simple method for checking if the arg is a single digit char
    def isDigit(self,char):
        return char >= '0' and char <= '9'
    
    #Simple method for checking if the arg is a letter
    def isAlpha(self,char):
        return (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') or char == '_'
    
    #Simple method for checking if the arg is either a letter or a number
    def isAlphaNumeric(self, char):
        return self.isAlpha(char) or self.isDigit(char)
    
    
    def isIdentifier(self, char):
        while self.isAlphaNumeric(self.peek()):
            self.advance()
        text = self.sourceCode[self.start : self.current]
        type = TokenType(self.keywords.get(text)) if self.keywords.get(text) else TokenType.IDENTIFIER
        self.addToken(type)
        
        
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
        elif char == ')':
            self.addToken(TokenType.RIGHT_PAREN)
        elif char == '{':
            self.addToken(TokenType.LEFT_BRACE)
        elif char == '}':
            self.addToken(TokenType.RIGHT_BRACE)
        elif char == ',':
            self.addToken(TokenType.COMMA)
        elif char == '.':
            self.addToken(TokenType.DOT)
        elif char == ';':
            self.addToken(TokenType.SEMICOLON)
        elif char == '-':
            self.addToken(TokenType.MINUS)
        elif char == '+':
            self.addToken(TokenType.PLUS)
        elif char == '*':
            self.addToken(TokenType.STAR)
        elif char == '!':
            self.addToken(TokenType.BANG_EQUAL if self.match('=') else TokenType.BANG)
        elif char == '=':
            self.addToken(TokenType.EQUAL_EQUAL if self.match('=') else TokenType.EQUAL)
        elif char == '<':
            self.addToken(TokenType.LESS_EQUAL if self.match('=') else TokenType.LESS)
        elif char == '>':
            self.addToken(TokenType.GREATER_EQUAL if self.match('=') else TokenType.GREATER)
        elif char == '/':
            #We read until we reach the end of line
            if self.match('/'):
                while self.peek() != '/n' and not self.isAtEnd():
                    self.advance()
            else:
                self.addToken(TokenType.SLASH)
        elif char == ' ':
            pass
        elif char == '\r':
            pass
        elif char == '\t':
            pass
        elif char == '\n':
            self.line += 1
        elif char == '"':
            self.readString()
        else:
            if self.isDigit(char):
                self.readNumber()
            elif self.isAlpha(char):
                self.isIdentifier(char)
            else: 
                print(f"Unexpected Character{char}" + " at line ", self.line)
        
        