# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, atleast , atmost):
            if not node: return True
            if node.val >= atmost or node.val <= atleast:
                return False
            return validate(node.left,atleast,min(node.val , atmost)) and validate(node.right,max(atleast, node.val),atmost)
        return validate(root,-inf,inf)
            