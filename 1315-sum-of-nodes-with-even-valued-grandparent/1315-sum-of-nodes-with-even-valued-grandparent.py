# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root: return
        self.ans = 0
        def dfs(node, parent , grandParent):
            if not node: return
            
            if grandParent and not grandParent.val % 2:
                self.ans += node.val
            
            dfs(node.right,node,parent)
            dfs(node.left,node,parent)
        dfs(root,None,None)
        return self.ans