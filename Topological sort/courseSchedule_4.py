class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegree = [0]*numCourses
        neighbour = defaultdict(set)
        for course in prerequisites:
            indegree[course[1]] += 1
            neighbour[course[0]].add(course[1])
        q = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append((i , set()))
        parents = [set() for _ in range(numCourses)]
        while q:
            cur , parent = q.pop()
            parent.add(cur)
            for neigh in neighbour[cur]:
                indegree[neigh] -= 1
                parents[neigh] = parents[neigh].union(parent)
                if indegree[neigh] == 0:
                    q.append((neigh , parents[neigh]))
        res = []
        for query in queries:
            if query[0] in parents[query[1]]:
                res.append(True)
            else:
                res.append(False)
        return res