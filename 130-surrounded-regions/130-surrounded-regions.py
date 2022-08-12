class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        stack = []
        visited = set()
        self.DIR = (1,0,-1,0,1)
        self.inbound = lambda row,col: 0<= row < len(board) and 0 <= col < len(board[0])
        def dfs(row,col):
            if board[row][col] == 'X': return
            if (row,col) in visited: return
            self.countO += 1
            visited.add((row,col))
            stack.append((row,col))
            for t in range(4):
                new_row ,new_col = row + self.DIR[t], col + self.DIR[t+1]
                if self.inbound(new_row,new_col):
                    dfs(new_row,new_col)
                else:
                    self.isBound = False

        for row in range(len(board)):
            for col in range(len(board[0])):
                self.isBound = True
                self.countO = 0
                if board[row][col] == 'X':
                    continue
                if (row,col) in visited: continue
                dfs(row,col)
                if not self.isBound:
                    i = 1
                    while i <= self.countO:
                        stack.pop()
                        i += 1
        for i in stack:
            board[i[0]][i[1]] = 'X'
        
                