class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            e , m , w = edge
            graph[e].append(( w,m ))
            graph[m].append(( w,e ))
        heap = [(0,n)]
        dist = [inf] * (n + 1)
        dist[n] = 0
        while heap:
            w , m = heappop(heap)
            for neigh in graph[m]:
                if w + neigh[0] < dist[neigh[1]]:
                    heappush(heap , (w + neigh[0] , neigh[1] ))
                    dist[neigh[1]] = w + neigh[0]
        heap = [(0,n)]
        @lru_cache(None)
        def dfs(node):
            if node == n: return 1
            c = 0
            for child in graph[node]:
                if dist[child[1]] < dist[node]:
                    c += dfs(child[1])
            return c
        return dfs(1) % (10**9 + 7)
     
        
        
            
         
        
        