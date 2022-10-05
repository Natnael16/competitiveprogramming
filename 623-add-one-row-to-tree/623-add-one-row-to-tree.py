# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val,left = root)
        def addRow(node, d):
            if not node: return 
            if d == depth - 1:
                left, right = node.left, node.right
                node.left = TreeNode(val,left=left)
                node.right = TreeNode(val,right=right)
                return
            addRow(node.left,d+1)
            addRow(node.right,d+1)
        addRow(root,1)
        return root
        
        