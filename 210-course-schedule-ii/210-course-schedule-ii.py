class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        topo_sort =deque([])
        indegree = [0] * numCourses
        graph = defaultdict(list)
        
        for fir , sec in prerequisites:
            graph[fir].append(sec)
            indegree[sec] += 1
        q= deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            cur = q.popleft()
            topo_sort.appendleft(cur)
            
            for neigh in graph[cur]:
                indegree[neigh] -= 1
                if not indegree[neigh]:
                    q.append(neigh)
        return topo_sort if numCourses == len(topo_sort) else [] 