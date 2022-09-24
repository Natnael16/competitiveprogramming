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
                if total == targetSum: self.ans.append(path)
                return
            
            cp = copy.deepcopy(path)
            cp2 = copy.deepcopy(path)
            fun(node.left , total , cp )
            fun(node.right, total , cp2)
        fun(root,0,[])
        return self.ans
            