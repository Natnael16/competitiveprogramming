class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        column_dict = defaultdict(list)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                column_dict[(len(matrix) - 1) - row].append(matrix[row][col])
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                matrix[c][r] = column_dict[r][c]
        