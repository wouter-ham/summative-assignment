class Amplify:
    source = ''
    output = ''

    def __init__(self, source: str):
        self.source = source

    def dec2bin(self: int) -> str:
        output = ''

        while self > 0:
            output = str(self % 2) + output
            self = self // 2

        return output

    def bin2dec(self: str) -> int:
        output = 0
        i = len(self) - 1
        while i >= 0:
            output = output * 2
            output = output + int(self[i])
            i = i - 1

        return output

    def calculate(self):
        return self
