class Solution:

    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        inbound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(
            grid[0])
        self.DIR = (0, 1, 0, -1, 0)

        self.cur_time = 0
        self.target = (len(grid) - 1, len(grid[0]) - 1)
        while heap:

            val, cur_row, cur_col = heapq.heappop(heap)
            # print(cur_row,cur_col)
            visited.add((cur_row, cur_col))
            if self.cur_time < grid[cur_row][cur_col]:
                self.cur_time += (grid[cur_row][cur_col] - self.cur_time)
            if (cur_col, cur_row) == self.target:
                return self.cur_time
            for i in range(4):
                new_row, new_col = self.DIR[i] + cur_row, self.DIR[i +
                                                                   1] + cur_col

                if inbound(new_row,
                           new_col) and (new_row, new_col) not in visited:
                    heapq.heappush(heap,
                                   (grid[new_row][new_col], new_row, new_col))
            # print(heap)

        return cur_time