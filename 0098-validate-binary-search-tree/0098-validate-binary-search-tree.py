# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode],atleast=-inf,atmost=inf) -> bool:
        
        if not root:
            return True
        if root.val >= atmost or root.val <= atleast:
            return False
        return self.isValidBST(root.left,atleast,min(root.val , atmost)) and \
                                self.isValidBST(root.right,max(atleast, root.val),atmost)
        
            