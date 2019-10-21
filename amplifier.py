class Amplifier:
    source: int = 0
    source_list: list = []
    unique_list: list = []
    amplified: tuple = ()

    def __init__(self, source: int):
        self.source = source
        self.source_list = [10] if len([int(x) for x in str(source)]) == 1 else [int(x) for x in str(source)]
        self.unique()

        # [10] if len([int(x) for x in str(source)]) == 1 else [int(x) for x in str(source)]

    def unique(self) -> list:
        for x in self.source_list:
            if x not in self.unique_list:
                self.unique_list.append(x)
        return self.unique_list

    def dec2bin(self, getal: int) -> str:
        output = ''

        while getal > 0:
            output = str(getal % 2) + output
            getal = getal // 2

        return output

    def bin2dec(self, string: str) -> int:
        output = 0
        i = len(string) - 1
        while i >= 0:
            output = output * 2
            output = output + int(string[i])
            i = i - 1

        return output

    def amplify(self):
        if int(self.source) > 0:
            self.amplified = (
                self.source,
                sum(self.unique_list),
                len(str(self.unique_list))
            )

            return self.amplified


for x in (1, 2, 12, 1221, 123456789, 123123123123456789999, 1359, 9531, 315191):
    print(Amplifier(x).amplify())

# print(Amplify(1298327111).unique())
