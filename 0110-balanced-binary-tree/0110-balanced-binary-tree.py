# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        @lru_cache(None)
        def maxHeight(node):
            if not node:
                return 0
            return max(maxHeight(node.left), maxHeight(node.right)) + 1
        if not root:
            return True
        left_d , right_d = maxHeight(root.left), maxHeight(root.right)
        return abs(left_d - right_d) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
            