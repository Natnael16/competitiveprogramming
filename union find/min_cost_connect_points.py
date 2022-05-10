class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        root = [i for i in range(len(points))]
        rank = [1] * len(points)

        def find(x):
            if x == root[x]: return x
            root[x] = find(root[x])
            return root[x]

        def union(x, y):
            r1, r2 = find(x), find(y)
            if r1 != r2:
                if rank[r1] > rank[r2]:
                    root[r2] = r1
                elif rank[r2] > rank[r1]:
                    root[r1] = r2
                else:
                    root[r1] = r2
                    rank[r2] += 1
        heap = []
        for row in range(len(points)):
            
            for col in range(row + 1,len(points)):
                # if point == cord: continue
                msum = abs(points[row][0] - points[col][0]) + abs( points[row][1] - points[col][1])
                heappush(heap , (msum ,row, col))
        heap.sort(key = lambda x:x[0])
        edges = 0
  
        while heap:
            w , r , c = heappop(heap)
            if find(r) != find(c):
                union(r , c)
                res += w
                edges += 1
                if edges == len(root) - 1:
                    break
              
        # print(root)
        return res