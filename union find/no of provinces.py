class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        root = [i for i in range(len(isConnected))]
        rank = [1] * len(isConnected)

        # print(root)
        def find(node):
            if node == root[node]:
                return node
            root[node] = find(root[node])
            return root[node]

        # print(find(2) , find(1))
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    root[root2] = root1
                elif rank[root1] < rank[root2]:
                    root[root1] = root2
                else:
                    root[root1] = root2
                    rank[root2] += 1

        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col] and col > row:
                    union(row, col)
        count = 0
        # print(root)
        for j in range(len(root)):
            if root[j] == j:
                count += 1
        return count