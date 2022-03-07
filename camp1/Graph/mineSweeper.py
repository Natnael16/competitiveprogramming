class Solution:

    def updateBoard(self, board: List[List[str]],
                    click: List[int]) -> List[List[str]]:
        self.Dir = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1),
                    (-1, 1), (1, -1)]
        inbound = lambda row, col: 0 <= row < len(board) and 0 <= col < len(
            board[0])

        visited = set()

        def dfs(row, col):
            visited.add((row, col))
            neighbours = []
            countB = 0
            for d in self.Dir:
                new_row, new_col = row + d[0], col + d[1]
                if inbound(new_row, new_col):
                    if board[new_row][new_col] == 'M':
                        # print("c")
                        countB += 1
                    if (new_row, new_col
                        ) not in visited and board[new_row][new_col] != 'M':
                        neighbours.append((new_row, new_col))
            # print(row,col)
            if countB == 0:
                board[row][col] = 'B'
                for n in neighbours:
                    if (n[0], n[1]
                        ) not in visited and not board[n[0]][n[1]].isdigit():
                        visited.add((n[0], n[1]))
                        dfs(n[0], n[1])
            else:
                board[row][col] = str(countB)

        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        dfs(click[0], click[1])
        return board