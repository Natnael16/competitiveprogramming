class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        child_count = defaultdict(int)
        initial = 0
        def count(node,parent,depth):
            nonlocal initial
            cur_count = 1
            initial += depth
            for neigh in graph[node]:
                if neigh != parent:
                    cur_count += count(neigh,node,depth + 1)
            child_count[node] = cur_count
            return cur_count
        count(0,-1,0)
        output = [0]*n
        def fillTable(node,parent, value):
            nonlocal initial
            output[node] = value

            for neigh in graph[node]:
                if neigh != parent:
                    your_value = value + -(child_count[neigh]) + abs(n - child_count[neigh])
                    fillTable(neigh,node,your_value)
        fillTable(0,-1,initial)

        

        return output
            