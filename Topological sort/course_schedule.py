class Solution:

    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        neighbour = defaultdict(set)
        for course in prerequisites:
            indegree[course[0]] += 1
            neighbour[course[1]].add(course[0])
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        count = 0
        while q:
            cur = q.popleft()
            count += 1
            for neigh in neighbour[cur]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        return count == numCourses