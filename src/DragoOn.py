from lexer.scanner import Scanner


class DragoOn:
    def __init__(self, sourceCode) -> None:
        self.scanner = Scanner(sourceCode=sourceCode)

    def run(self):
        self.scanner.scan()
