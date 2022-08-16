class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for n1 , n2 , time in roads:
            graph[n1].append((n2 , time))
            graph[n2].append((n1 , time))
            
        ways = [0] * (n)
        times = [sys.maxsize] * (n)
        ways[0] , times[0] = 1 , 0
        
        heap = [(0 , 0)]  # node , time
        
        while heap:
            time , node = heappop(heap)
            
            for neigh , takes in graph[node]:
                cur_time = takes + time
                if cur_time < times[neigh]:
                    times[neigh] = cur_time
                    ways[neigh] = ways[node]
                    heappush(heap , ( cur_time , neigh))
                elif cur_time == times[neigh]:
                    ways[neigh] += ways[node]
        print(ways)
        return ways[-1] % (10**9 + 7)
            
        