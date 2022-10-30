class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for idx , edge in enumerate(times):
            u ,v , w = edge
            graph[u].append((w,v))
        dist = [inf] * (n + 1)
        heap = [(0,k)]
       
        visited = set()
        while heap:
            cur_dist, node = heappop(heap)
            visited.add(node)
            for takes, neigh in graph[node]:
                if neigh not in visited:
                    calculated_dist = cur_dist + takes
                    dist[neigh] = min(dist[neigh] , calculated_dist)
                    heappush(heap, (calculated_dist, neigh))
                
        maxi= -inf
        for d in dist:
            if d != inf:
                maxi =max(maxi,d)
        if len(visited) != n or maxi == -inf:
            return -1
        return maxi
                
                