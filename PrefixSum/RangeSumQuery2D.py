class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.hash_table = {}
        self.prefix_map()
    def prefix_map(self):
        for i in range(len(self.matrix)):
            pre_sum = 0
            arr = []
            for j in range(len(self.matrix[i])):
                pre_sum += self.matrix[i][j]
                arr.append(pre_sum)
            self.hash_table[i] = arr
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        psum = 0
        while row1 <= row2:
            if col1 == 0:
                psum += self.hash_table[row1][col2]
            else:
                psum += self.hash_table[row1][col2] - self.hash_table[row1][col1-1]
            row1 += 1
        return psum