# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node , less , greater):
            if not node: return True
            
            if node.val >= less or node.val <= greater: return False
            left = helper(node.left , min(less, node.val) , greater)
            right = helper(node.right , less , max(greater , node.val))
            return left and right
        
        return helper(root , float("inf") , -float("inf"))
            