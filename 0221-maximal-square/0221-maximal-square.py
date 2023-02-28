class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n ,m = len(matrix), len(matrix[0])
        dp = [[0] * (m + 1) for _ in range(n+1)]
        
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == '1':
                    dp[row + 1][col + 1] = min(dp[row][col + 1], dp[row + 1][col], dp[row][col]) + 1
        
        return max([max(row) for row in dp]) ** 2