class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        inbound = lambda x,y: 0 <= x < n and 0 <= y < m
        indegree = [[0]*m for i in range(n)] 
      
        ad_list = defaultdict(list)
        dirs = [0,1,0,-1,0]
        for row in range(n):
            for col in range(m):
                for d in range(4):
                    new_row = row + dirs[d]
                    new_col = col + dirs[d + 1]
                    if inbound(new_row , new_col) and matrix[new_row][new_col] > matrix[row][col]:
                        indegree[new_row][new_col] += 1
                        ad_list[(row, col)].append((new_row , new_col))
        q = deque([])
        
        for r in range(n):
            for c in range(m):
                if indegree[r][c] == 0:
                    q.append((r,c))
        @lru_cache(None)
        def dfs(ind):
            if not ad_list[ind]:
                return 1
            maxi = -inf
            for i in ad_list[ind]:
                maxi = max(maxi , 1 + dfs(i)) 
            return maxi
            
        maxi = -inf
        for vals in q:
            maxi = max(maxi, dfs(vals))
        return maxi
            
                
                