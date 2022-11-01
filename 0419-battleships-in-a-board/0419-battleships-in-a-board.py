class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(row, col , rows, cols, visited, board):
            visited.add((row,col))
            if row + 1 < rows and board[row + 1][col] == "X":
                dfs(row + 1, col,rows,cols,visited,board)
            elif col + 1 < cols and board[row][col + 1] == "X":
                dfs(row, col + 1,rows,cols,visited,board)
            
        def main(board):
            count = 0
            visited = set()
            rows , cols = len(board), len(board[0])
            for row in range(rows):
                for col in range(cols):
                    
                    if board[row][col] != "." and (row,col) not in visited:
                        dfs(row, col,rows, cols , visited, board)
                        count += 1
            return count
        return main(board)