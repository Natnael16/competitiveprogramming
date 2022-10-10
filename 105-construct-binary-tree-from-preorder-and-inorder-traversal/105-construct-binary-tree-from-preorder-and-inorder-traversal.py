# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder: return None
                
        root = TreeNode(preorder[0])
        mid_ind = inorder.index(preorder[0])
        
        l_inorder = inorder[:mid_ind]
        r_inorder = inorder[mid_ind + 1:]
        r_preorder = preorder[mid_ind + 1 :]
        l_preorder = preorder[1:mid_ind + 1] 
        
        root.left = self.buildTree(l_preorder,l_inorder)
        root.right = self.buildTree(r_preorder, r_inorder)
        return root
        
        
        
        