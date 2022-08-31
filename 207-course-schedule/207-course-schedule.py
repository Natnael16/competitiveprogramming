class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)
        
        q = deque([])
        
        for first , second in prerequisites:
            graph[first].append(second)
            indegree[second] += 1
        for i in range(numCourses):
            if indegree[i] == 0: q.append(i)
        while q:
            cur = q.popleft()
            for neigh in graph[cur]:
                indegree[neigh] -= 1
                if not indegree[neigh]: q.append(neigh)
        for i in indegree:
            if i != 0: return False
        return True