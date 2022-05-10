class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        root = [i for i in range(len(accounts))]
        rank = [1] * len(accounts)

        def find(x):
            if x == root[x]: return x
            root[x] = find(root[x])
            return root[x]

        def union(x, y):
            r1, r2 = find(x), find(y)

            if r1 != r2:
                if rank[r1] > rank[r2]:
                    root[r2] = r1
                elif rank[r2] > rank[r1]:
                    root[r1] = r2
                else:
                    root[r1] = r2
                    rank[r2] += 1

        visited = {}
        for i, emails in enumerate(accounts):
            for email in emails[1:]:
                if email in visited:
                    union(visited[email], i)
                else:
                    visited[email] = i

        unique_elmts = defaultdict(set)

        for r in range(len(root)):
            for acc in accounts[r][1:]:
                unique_elmts[find(r)].add(acc)
        res = []
        for key in unique_elmts.keys():
            res.append([accounts[key][0]] + sorted(list(unique_elmts[key])))
        return res