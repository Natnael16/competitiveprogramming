class Solution:
    def canChange(self,row, col, isChanged,rows, cols,board):
        dirs = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
        count = 0
        for add_row, add_col in dirs:
            new_row, new_col = row + add_row, col + add_col
            if 0 <= new_row < rows and 0 <= new_col < cols:
                cur_val = board[new_row][new_col]
                if (new_row, new_col) in isChanged:
                    cur_val = 1 - cur_val
                if cur_val == 1:
                    count += 1
        if board[row][col] == 0 and count == 3:
            return True
        elif board[row][col] == 1 and (count < 2 or count > 3):
            return True
        return False
                
        
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        changed = set()
        rows ,cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                destiny = self.canChange(row, col,changed, rows, cols ,board)
                if destiny:
                    changed.add((row, col))
                    board[row][col] = 1 - board[row][col]
                    
                
                    