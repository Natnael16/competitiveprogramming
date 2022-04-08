class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        self.DIR = (1,0,-1,0,1)
        self.inbound = lambda row,col: True if 0 <= row < len(grid) and 0 <= col < len(grid[0]) else False
        def dfs(row,col):
            if not grid[row][col]: return
            self.countLand += 1
            
            for t in range(4):
                new_row ,new_col = row + self.DIR[t], col + self.DIR[t+1]
                if self.inbound(new_row,new_col):
                    grid[row][col] = 0
                    dfs(new_row,new_col)
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                self.countLand = 0
                if grid[row][col] == 0:
                    continue
                
                dfs(row,col)
                maxArea = max(maxArea,self.countLand)
        return maxArea
