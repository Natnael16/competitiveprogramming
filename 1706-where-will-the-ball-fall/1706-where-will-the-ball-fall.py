class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        answer = []
        rows, cols = len(grid), len(grid[0])
        def stuck(row,col):
            if grid[row][col] == 1 and ((col + 1) >= cols or grid[row][col + 1] == -1):
                return True
            elif grid[row][col] == -1 and ((col - 1) < 0 or grid[row][col - 1] == 1):
                return True
            return False
        def canReach(row,col):
            if row >= rows:
                return col
            if stuck(row,col):
                return -1
            if grid[row][col] == 1:
                return canReach(row + 1, col + 1)
            else:
                return canReach(row + 1, col - 1)
 
        for col in range(cols):
            answer.append(canReach(0,col))
        return answer