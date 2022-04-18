class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
      
        root = []
        for i in range(len(grid)):
            a = []
            for j in range(len(grid[0])):
                a.append((i,j))
            root.append(a)
        
        rank = defaultdict(int)
        inbound = lambda x , y : 0 <= x < len(grid) and 0 <= y < len(grid[0])
        DIR = [1,0,-1,0,1]
        def find(x):
            if root[x[0]][x[1]] == x:
                return x
            # print(x)
            root[x[0]][x[1]]
            
            grid[x[0]][x[1]] = find(root[x[0]][x[1]])
            return grid[x[0]][x[1]]
        def union(x , y):
            # print(x , y)
            r1 = find(x)
            r2 = find(y)
            # print(r1 , r2)
            if r1 != r2:
                if rank[r1] > rank[r2]:
                    root[r2[0]][r2[1]] = r1
                    rank[r1] += rank[r2] + 1
                    rank[r2] = 0
                elif rank[r1] < rank[r2]:
                    root[r1[0]][r1[1]] = r2
                    rank[r2] += rank[r1] + 1
                    rank[r1] = 0
                else:
                    root[r2[0]][r2[1]] = r1
                    rank[r1] += rank[r2] + 1
                    rank[r2] = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    for d in range(4):
                        if inbound(row + DIR[d] , col + DIR[d + 1]) and grid[row + DIR[d]][col + DIR[d + 1]]:
                            # print(row, col,'yyyy' , row + DIR[d], col + DIR[d + 1])
                            union((row, col) , (row + DIR[d] , col + DIR[d + 1]))
        # print(rank)
        return max(rank.values()) + 1 if rank.values() else max(max(grid))
                
       
        