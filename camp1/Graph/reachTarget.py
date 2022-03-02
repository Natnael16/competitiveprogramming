class Solution:

    def reachTarget(self, node, sums, target):
        if not node: return
        if sums == target and not node.left and not node.right:
            # print('here')
            self.isTrue = True
        # print(sums)
        if node.right:
            self.reachTarget(node.right, sums + node.right.val, target)
        if node.left:
            self.reachTarget(node.left, sums + node.left.val, target)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return
        self.isTrue = False
        self.reachTarget(root, root.val, targetSum)
        return self.isTrued