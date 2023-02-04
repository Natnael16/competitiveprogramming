# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        self.getPaths(root,"",result)
            
        return result
        
    def getPaths(self,node,path, result):
        if not node:
            return
        if not node.left and not node.right:
            result.append(path + f"{node.val}")
            return
        
        self.getPaths(node.left,path + f"{node.val}" + "->",result)
       
        self.getPaths(node.right,path + f"{node.val}" + "->" ,result)
        
        
        