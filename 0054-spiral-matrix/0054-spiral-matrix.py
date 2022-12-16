class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        rows, cols = len(matrix), len(matrix[0])
        valid = lambda row, col : (row, col)  not in visited and 0 <= row < rows and 0 <= col < cols
        self.out = []
        dirs = [(0, 1), (1,0), (0,-1), (-1,0)] # right, down, left , up

        def dfs(row, col, direction):
            
            visited.add((row, col))
            next_row , next_col = dirs[direction][0] + row, dirs[direction][1] + col
            next_next_row , next_next_col = dirs[(direction + 1) % 4][0] + row, dirs[(direction + 1) % 4][1] + col
            
            if not valid(next_row, next_col) and valid(next_next_row, next_next_col):
                    dfs(row , col , (direction + 1) % 4)
            elif not valid(next_row, next_col) and  not valid(next_next_row, next_next_col):
                self.out.append(matrix[row][col])
            else:
                self.out.append(matrix[row][col])
                dfs(next_row, next_col, direction)
        dfs(0,0,0)
        return self.out



