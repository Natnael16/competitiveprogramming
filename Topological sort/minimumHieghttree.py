class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        children = [set() for i in range(n)]
        
        for i , j in edges:
            children[i].add(j)
            children[j].add(i)
        if n == 1: return [0]
        if n == 2: return [0,1]
        q = deque()
        
        for ind , ch in enumerate(children):
            if len(ch) == 1:
                q.append(ind)

        nodes = n
        while nodes > 2:
            leaves = []
            nodes -= len(q)
            while q:
                cur = q.pop()
                to_delete = children[cur].pop()
                
                children[to_delete].discard(cur)
                
                if len(children[to_delete]) == 1:
                    leaves.append(to_delete)
            q = leaves
        return q      