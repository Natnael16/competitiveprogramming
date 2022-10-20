# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        def getMaxLength(node):
            if not node:
                return 0
            target = node.val
            
            left_calculated = 0
            right_calculated = 0
            
            if  node.left and node.left.val == target:
                left_calculated = 1 + getMaxLength(node.left)
            else:
                getMaxLength(node.left)
                
            if node.right and node.right.val == target:
                right_calculated = 1 + getMaxLength(node.right)
            else:
                getMaxLength(node.right)
                
            max_candidate = left_calculated + right_calculated
            self.max_length = max(self.max_length,max_candidate)
            
            return max(left_calculated,right_calculated)
            
            
    
        self.max_length = 0
        getMaxLength(root)

        return self.max_length
            