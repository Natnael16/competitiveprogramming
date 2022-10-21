# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def dp(node):
            
            if not node: return 0
            rob = node.val
            
            if node.left:
                rob  += dp(node.left.left) + dp(node.left.right)
                
            if node.right:
                rob += dp(node.right.left) + dp(node.right.right)
            
            dont_rob = dp(node.right) + dp(node.left)
            
            return max(rob,dont_rob)

        return dp(root)