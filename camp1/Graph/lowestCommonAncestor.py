from functools import lru_cache


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @lru_cache
    def get_height(self, node, depth=0):
        if not node: return depth - 1
        # if not node.left and node.right: return depth
        left = self.get_height(node.left, depth + 1)
        right = self.get_height(node.right, depth + 1)

        return (max(left, right))

    @lru_cache
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if self.get_height(root.left) > self.get_height(root.right):
            return self.lcaDeepestLeaves(root.left)
        elif self.get_height(root.right) > self.get_height(root.left):
            return self.lcaDeepestLeaves(root.right)
        else:
            return root