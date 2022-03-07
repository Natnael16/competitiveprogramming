import heapq


class Solution:

    def robot_factory(self, grid):
        visited = set()
        heap = []


        def isValid(num):
            res = []
            b = str(format(num, 'b'))
            while len(b) < 4:
                b = '0' + b

            if b[0] == 0:
                res.append([-1, 0])
            if b[1] == 0:
                res.append([0, 1])
            if b[2] == 0:
                res.append([1, 0])
            if b[3] == 0:
                res.append([0, -1])
            return res

        def dfs(row, col):
            if (row, col) in visited: return
            valid = isValid(grid[row][col])
            self.rooms += 1
            visited.add((row, col))
            for i in valid:
                new_row, new_col = row + i[0], col + i[1]
                if (new_row, new_col) not in visited:
                    dfs(new_row, new_col)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited:

                    self.rooms = 0
                    dfs(row, col)
                    heapq.heappush(heap, -self.rooms)
        print(heap, visited)
        for j in heap:
            print(-heapq.heappop(heap), end=' ')


size = list(map(int, input().split()))
ground = []
for i in range(size[0]):
    line = list(map(int, input().split()))
    ground.append(line)
print(ground)
sol = Solution()
sol.robot_factory(ground)