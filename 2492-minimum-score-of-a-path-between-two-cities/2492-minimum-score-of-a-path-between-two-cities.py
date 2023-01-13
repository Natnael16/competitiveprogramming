class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v , w in roads:
            graph[u].append((v, w))
            graph[v].append((u , w))
            
        queue = deque([(1, inf)])
        visited = set()
        min_so_far = inf
        while queue:
            cur_road, weight = queue.popleft()
            min_so_far = min(min_so_far, weight)
            visited.add(cur_road)
            for neigh , w_new in graph[cur_road]:
                if neigh not in visited:
                    queue.append((neigh, w_new))
                    
        return min_so_far
                    
                
        
        