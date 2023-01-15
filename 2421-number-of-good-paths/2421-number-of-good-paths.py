class Solution:
    
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        arr_len = len(vals)
        edges.sort(key = lambda edge : max(vals[edge[0]],vals[edge[1]]))
        root = [i for i in range(arr_len)]
        max_rank = [Counter([val]) for val in vals]
        self.score = 0
        def find(node):
            if root[node] == node:
                return node
            root[node] = find(root[node])
            return root[node]
        
        def union(nodeOne, nodeTwo):
            rootOne, rootTwo  = find(nodeOne), find(nodeTwo)
            if rootOne != rootTwo:
                
                max_val = max(vals[rootOne],vals[rootTwo])
                if vals[rootOne] > vals[rootTwo]:
                    root[rootTwo] = rootOne
                elif vals[rootTwo] > vals[rootOne]:
                    root[rootOne] = rootTwo
                else:
                    self.score += max_rank[rootOne][vals[rootOne]] * max_rank[rootTwo][vals[rootTwo]]
                    max_rank[rootOne][vals[rootOne]] += max_rank[rootTwo][vals[rootTwo]]
                    root[rootTwo] = rootOne
        for u ,v in edges:
            union(u, v)
        return self.score + arr_len
        
        
                  