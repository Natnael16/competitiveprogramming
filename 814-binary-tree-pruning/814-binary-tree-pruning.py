# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        @lru_cache(None)
        def isOnlyZero(node):
            if not node: return True
            if node.val == 1: return False
            
            return isOnlyZero(node.left) and isOnlyZero(node.right)
        
        if isOnlyZero(root): return 
        def dfs(node):
            if not node: return 
            if isOnlyZero(node.left): node.left = None
            if isOnlyZero(node.right): node.right = None
            
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return root
    
            