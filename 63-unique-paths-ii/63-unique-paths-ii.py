class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
                
        n,m = len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1: return 0
        
        for row in range(n):
            for col in range(m):
                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = -1
        obstacleGrid[0][0] = 1
        for row in range(n):
            for col in range(m):
                if obstacleGrid[row][col] == -1: continue
                #right
                if col + 1 < m and obstacleGrid[row][col + 1] != -1:
                    
                    obstacleGrid[row][col + 1] += obstacleGrid[row][col]
                # down
                if row + 1 < n and obstacleGrid[row + 1][col] != -1:
                    
                    obstacleGrid[row + 1][col] += obstacleGrid[row][col]
        
        return obstacleGrid[-1][-1]