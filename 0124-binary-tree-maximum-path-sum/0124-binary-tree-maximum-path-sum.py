# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_of_all = -float('inf')
        def getMaxPath(node):
            nonlocal max_of_all
            if not node: return 0
            leftValue  = getMaxPath(node.left)
            rightValue = getMaxPath(node.right)
            
            maxPathSum = max(leftValue + node.val, rightValue + node.val ,node.val, leftValue + rightValue + node.val)
            max_of_all = max(max_of_all , maxPathSum)
            
            return max(node.val, leftValue + node.val , rightValue + node.val)
        
        getMaxPath(root)
        
        return max_of_all