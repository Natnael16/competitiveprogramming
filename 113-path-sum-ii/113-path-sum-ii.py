# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        def fun(node, total, path ):
            if not node: return
            total += node.val
            path.append(node.val)
            if not node.left and not node.right:
                if total == targetSum: self.ans.append(path.copy())
            else:
                fun(node.left , total , path)
                fun(node.right, total , path)
            path.pop()
    
        fun(root,0,[])
        return self.ans
            