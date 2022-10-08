class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len , col_len = len(grid), len(grid[0])
        directions = (1,0,-1,0,1)
        def inbound(row, col):
            return 0 <= row < row_len and 0 <= col < col_len
        
        def dfs(row, col):
            if not inbound(row, col): return 
            if grid[row][col] == "0": return 
            grid[row][col] = "0"
            for d in range(len(directions) - 1):
                new_row , new_col = row + directions[d],col + directions[d + 1]
                dfs(new_row, new_col)
                
            
    
        count = 0
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == "1":
                    dfs(row,col)
                    count +=1
    
        return count
        
        
        