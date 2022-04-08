class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        view = set()
        time = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    q.append([(row, col), 0])

        DIR = (0, 1, 0, -1, 0)

        def isValid(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(
                    grid[0]) and (row, col) not in view:
                return True

        while q:
            pos, time = q.popleft()
            view.add(pos)
            for i in range(4):
                new_row, new_col = pos[0] + DIR[i], pos[1] + DIR[i + 1]
                if isValid(new_row, new_col) and grid[new_row][new_col] == 1:
                    q.append([(new_row, new_col), time + 1])
                    view.add((new_row, new_col))
                elif isValid(new_row,
                             new_col) and (grid[new_row][new_col] == 2
                                           or grid[new_row][new_col] == 0):
                    view.add((new_row, new_col))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in view and grid[row][col] == 1:
                    return -1
        return time