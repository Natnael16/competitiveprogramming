class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
            count = 0
            rows , cols = len(board), len(board[0])
    
            for row in range(rows):
                for col in range(cols):
                    if board[row][col] != ".":
                        if (row - 1 < 0 or board[row - 1][col] == ".")  and (col - 1 < 0 or board[row][col - 1] == "."):
                            count += 1
            return count