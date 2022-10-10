# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node, sum_):
            if not node: return sum_
            
            r_sum = dfs(node.right,sum_) + node.val
            node.val = r_sum
            l_sum = dfs(node.left,r_sum)
            
            return l_sum
        dfs(root,0)
        return root
        
            