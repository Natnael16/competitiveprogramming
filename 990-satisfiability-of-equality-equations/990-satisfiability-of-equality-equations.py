class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        root = [i for i in range(26)]
        rank = [1] * 26
        s = "abcdefghijklmnopqrstuvwxyz"
        index = {}
        for i, ch in enumerate(s): index[ch] = i
        
        def find(node):
            if node == root[node]: return node
            root[node] = find(root[node])
            return root[node]
        def union(node1,node2):
            r1,r2 = find(node1), find(node2)
            if r1 != r2:
                if rank[r1] > rank[r2]:
                    root[r2] = r1
                elif rank[r1] < rank[r2]:
                    root[r1] = r2
                else:
                    root[r1] = r2
                    rank[r2] += 1
        ans = True
        unequal = []
        for e in equations:
            if e[1] + e[2] == "==": union(index[e[0]], index[e[-1]])
            else: unequal.append(e)
 
        for une in unequal:
            if find(index[une[0]]) == find(index[une[-1]]): ans = False
        return ans