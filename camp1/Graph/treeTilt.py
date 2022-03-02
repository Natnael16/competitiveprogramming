class Solution:

    def tilt(self, node):
        if node == None: return 0
        if not node.left and not node.right:
            return node.val
        left = self.tilt(node.left)
        right = self.tilt(node.right)
        self.tot_diff += abs(left - right)
        return left + right + node.val

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tot_diff = 0
        self.tilt(root)
        return self.tot_diff