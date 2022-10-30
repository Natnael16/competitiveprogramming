class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        dist = [0] * n
        dist[start] = 1
        heap = [(-1,start)]
        graph = defaultdict(list)
        for idx , edge in enumerate(edges):
            graph[edge[0]].append((edge[1], succProb[idx]))
            graph[edge[1]].append((edge[0] , succProb[idx]))
        visited = set()
        while heap:
            path, cur = heappop(heap)
            path = -path
            visited.add(cur)
            if cur == end:
                return path
            for neigh , d in graph[cur]:
                if neigh not in visited:
                    calculated_dist = path * d
                    dist[neigh] = max(dist[neigh], calculated_dist)
                    heappush(heap,(-calculated_dist ,neigh))
        return 0
        