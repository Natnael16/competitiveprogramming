class Solution:
    def dfs(self, grid, i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '#'
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i, j-1)
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [0,1,0,-1,0]
        inbound = lambda x , y : 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    self.dfs(grid , row , col)
                
        return count 
