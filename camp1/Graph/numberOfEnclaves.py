class Solution:

    def numEnclaves(self, grid: List[List[int]]) -> int:
        DIR = (1, 0, -1, 0, 1)
        inbound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(
            grid[0])
        self.countCells = 0

        def dfs(row, col):
            if not grid[row][col]: return
            grid[row][col] = 0
            self.countL += 1
            for i in range(4):
                new_row, new_col = row + DIR[i], col + DIR[i + 1]
                if inbound(new_row, new_col):
                    if grid[new_row][new_col]:
                        dfs(new_row, new_col)
                else:
                    self.flag = False

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                self.flag = True
                self.countL = 0
                if not grid[row][col]:
                    continue
                dfs(row, col)
                if self.flag == True:
                    self.countCells += self.countL
        return self.countCells