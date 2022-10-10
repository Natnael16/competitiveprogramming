# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder: return
        
        root = TreeNode(postorder[-1])
        mid_ind = inorder.index(postorder[-1])
        left_inord = inorder[:mid_ind]
        right_inord = inorder[mid_ind+ 1:]
        
        right_postord = postorder[mid_ind: -1]
        left_postord = postorder[:len(left_inord)]
        
        root.left = self.buildTree(left_inord,left_postord)
        root.right = self.buildTree(right_inord,right_postord)
        return root
        
        