class Amplifier:
    source: int = 0
    source_list: list = []
    unique_list: list = []
    amplified: tuple = ()

    def __init__(self, source: int):
        self.source = source
        self.source_list = [int(x) for x in str(source)]
        self.unique()

    def unique(self) -> list:
        self.unique_list = list(set(self.source_list))
        return self.unique_list

    def amplify(self):
        if int(self.source) > 0:
            self.amplified = (
                self.source,
                sum(self.unique_list),
                10 if len(self.unique_list) == 1 else len(self.unique_list),

            )

            return self.amplified


for x in (1, 2, 12, 1221, 123456789, 123123123123456789999, 1359, 9531, 315191):
    print(Amplifier(x).amplify())
