class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        stones_len = len(stones)
        root = [i for i in range(stones_len)]
        rank = [1] * len(stones)
        row_map = defaultdict(list)
        col_map = defaultdict(list)
        for ind, stone in enumerate(stones):
            x,y = stone
            row_map[x].append(ind)
            col_map[y].append(ind)
            
        def find(node):
            if root[node] == node: return node
            root[node] = find(root[node])
            return root[node]
        
        def union(n1, n2):
            r1, r2 = find(n1), find(n2)
            if r1 != r2:
                if rank[r1] > rank[r2]:
                    root[r2] = r1
                    rank[r1] += rank[r2]
                elif rank[r2] > rank[r1]:
                    root[r1] = r2
                    rank[r2] += rank[r1]
                else:
                    root[r1] = r2
                    rank[r2] += rank[r1]
        for row in row_map:
            same_row = row_map[row]
            for i in range(len(same_row) - 1):
                union(same_row[i], same_row[i + 1])
        for col in col_map:
            same_col = col_map[col]
            for j in range(len(same_col) - 1):
                union(same_col[j], same_col[j + 1])
        seen = set()
        ans = 0
        for r in root:
            upmost = find(r)
            if upmost not in seen:
                ans += rank[upmost] - 1
                seen.add(upmost)
        return ans
                
            
    