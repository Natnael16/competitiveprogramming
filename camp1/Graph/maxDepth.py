class Solution:

    def dfs(self, node, depth):
        if node == None: return
        self.max_depth = max(depth, self.max_depth)
        for child in node.children:
            self.dfs(child, depth + 1)

    def maxDepth(self, root: 'Node') -> int:
        self.max_depth = 0
        if root == None: return 0
        self.dfs(root, 1)
        return self.max_depth