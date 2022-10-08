class Solution(object):
    def pacificAtlantic(self, matrix):
        
        pacific = set()
        atlantic = set()
        len_row, len_col = len(matrix), len(matrix[0])
        dirs = (1,0,-1,0,1)
        def bfs(q,visited):
            while q:
                row , col = q.popleft()
                if (row, col) in visited:
                    continue
                visited.add((row,col))
                for d in range(4):
                    new_row, new_col = row + dirs[d],col + dirs[d+1]
                    
                    if 0 <= new_row < len_row and 0 <= new_col < len_col and (new_row , new_col) not in visited:
                        if matrix[new_row][new_col] >= matrix[row][col]:
                            q.append((new_row, new_col))
                
                        
        for col in range(len_col):
            bfs(deque([(0, col)]), pacific)
            bfs(deque([(len_row - 1, col)]), atlantic)
            
        for row in range(len_row):
            bfs(deque([(row, 0)]), pacific)
            bfs(deque([(row, len_col - 1)]), atlantic)
            
        return (pacific & atlantic)
            
        
                
                
                