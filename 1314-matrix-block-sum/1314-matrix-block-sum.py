class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        dp = copy.deepcopy(mat)

        for row in range(n):
            for col in range(m):
                dp[row][col] += (dp[row][col-1] if col > 0 else 0)
            print(dp[row])
        
        for col in range(m):
            for row in range(n):
                dp[row][col] += (dp[row-1][col] if row > 0 else 0)
        
                        
        for row in range(n):
            for col in range(m):
                x1, x2 = max(0, col - k), min(col + k, m - 1)
                y1, y2 = max(0, row - k), min(row  + k, n - 1)
                dy = dp[y1-1][x2] if y1 > 0 else 0
                dx = dp[y2][x1-1] if x1 > 0 else 0
                dz = dp[y1-1][x1-1] if (x1 > 0 and y1 > 0) else 0
                mat[row][col] = dp[y2][x2] - dy - dx + dz

        return mat