# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def dp(node, can_rob):
            
            if not node: return 0
            
            if not can_rob:
                return dp(node.left,not can_rob) + dp(node.right,not can_rob)
            
            rob_left , pass_left = dp(node.left,not can_rob) , dp(node.left, can_rob)
            rob_right , pass_right =  dp(node.right,not can_rob) , dp(node.right, can_rob)
            
            return max(node.val + rob_left + rob_right, pass_left + pass_right)
            
        return dp(root,True)