class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        inbound = lambda r , c : 0<= r < len(grid) and 0 <= c < len(grid[0])
        Dirs = [1,0,-1,0,1]
        self.count = 0
        visited = set()
        def dfs(row, col):
            visited.add((row, col))
            for d in range(4):
                new_row, new_col = row + Dirs[d], col + Dirs[d + 1]
                
                if not inbound(new_row, new_col) or inbound(new_row, new_col) and grid[new_row][new_col] == 0:
                    
                    self.count += 1
                    
                elif grid[new_row][new_col] == 1:
                    if (new_row, new_col) not in visited:
                        dfs(new_row,new_col)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0: continue
                else:
                    
                    dfs(r,c)
                    return self.count
        
            
        