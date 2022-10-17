class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0] * (n + 1)
        for pre , nxt in relations:
            graph[pre].append(nxt)
            indegree[nxt] += 1
        
        heap = []
        for i in range(1,n + 1):
            if not indegree[i]:
                heappush(heap,(time[i - 1],i))
        
        offset = 0 
        while heap:
            month, course = heappop(heap)
            offset = month
            for neighbour in graph[course]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    heappush(heap,(time[neighbour - 1] + offset, neighbour))
        return offset
            
            
            
            
            
        
            