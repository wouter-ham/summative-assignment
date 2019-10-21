import string


class Amplifier:
    source: int = 0
    source_list: list = []
    unique_list: list = []
    amplified: tuple = ()
    digs = string.digits + string.ascii_letters

    def __init__(self, source: int):
        self.source = source
        self.source_list = [int(x) for x in str(source)]
        self.unique_list = list(set(self.source_list))

    def amplify(self) -> tuple:
        if self.source > 0:
            self.amplified = (
                self.source,
                sum(self.unique_list),
                10 if len(self.unique_list) == 1 else len(self.unique_list),
                self.int2base(sum(self.unique_list), 10 if len(self.unique_list) == 1 else len(self.unique_list))
            )

            return self.amplified

    def int2base(self, number, base):
        if number < 0:
            sign = -1
        elif number == 0:
            return self.digs[0]
        else:
            sign = 1

        number *= sign
        digits = []

        while number:
            digits.insert(0, self.digs[int(number % base)])
            number = int(number / base)

        if sign < 0:
            digits.insert(0, '-')
        return int(''.join(digits))


for x in (1, 2, 12, 1221, 123456789, 123123123123456789999, 1359, 9531, 315191):
    print(Amplifier(x).amplify())
