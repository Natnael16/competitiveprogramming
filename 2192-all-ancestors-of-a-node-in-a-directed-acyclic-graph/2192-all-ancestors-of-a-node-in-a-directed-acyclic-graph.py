from sortedcontainers import SortedList
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = [SortedList() for _ in range(n)]
        indegree = [0] * n
        
        graph = defaultdict(list)
        for frum , to in edges:
            graph[frum].append(to)
            indegree[to] += 1
        q = deque([])
        for i,count in enumerate(indegree):
            if count == 0:
                q.append(i)
        while q:
            cur_node = q.popleft()
            
            for neigh in graph[cur_node]:
                ancestors[neigh].add(cur_node)
                for ans in ancestors[cur_node]:
                    if ans not in ancestors[neigh]:
                        ancestors[neigh].add(ans)
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        return ancestors
            
        