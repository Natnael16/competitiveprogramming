class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        neighbour = defaultdict(set)
        indegree = [0]* n
        for edge in edges:
            neighbour[edge[0]].add(edge[1])
            indegree[edge[1]] += 1
        q = []
        res = [set() for _ in range(n)]
        for i , val in enumerate(indegree):
            if val == 0: q.append((i , set()))
       
        while q:
            cur , parents = q.pop()
            parents.add(cur)
            for neigh in neighbour[cur]:
                indegree[neigh] -= 1
                res[neigh] = res[neigh].union(parents)
                if indegree[neigh] == 0:
                    q.append((neigh , res[neigh]))
        for ind , val in enumerate(res):
            val.discard(ind)
            res[ind] = sorted(list(val))
        return res