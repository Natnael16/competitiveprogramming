# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        self.insert(root, val)
        return root
        
    def insert(self,root,value):
        
        # base case
        if value > root.val and not root.right:
            root.right = TreeNode(value)
        elif value < root.val and not root.left:
            root.left = TreeNode(value)
        elif value > root.val:
            self.insert(root.right, value)
            
        elif value < root.val:
            self.insert(root.left, value)
        
            
        
    
        
        
        