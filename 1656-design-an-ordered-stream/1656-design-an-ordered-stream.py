class OrderedStream:

    def __init__(self, n: int):
        self.pointer = 0
        self.limit = n
        self.stream = [0] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value
        result = []
        while self.pointer < self.limit and self.stream[self.pointer] != 0:
            result.append(self.stream[self.pointer])
            self.pointer += 1
        return result