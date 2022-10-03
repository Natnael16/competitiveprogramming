class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]* m for _ in range(n)]
        
        grid[0][0] = 1
        for row in range(n):
            for col in range(m):
                #right
                if col + 1 < m:
                    grid[row][col + 1] += grid[row][col]
                # bottom
                if row + 1 < n:
                    grid[row + 1][col] += grid[row][col]
        return grid[-1][-1]