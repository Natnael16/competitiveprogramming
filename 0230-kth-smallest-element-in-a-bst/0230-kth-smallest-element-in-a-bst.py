# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur  = 0
        ans = 0
        def inorder(node):
            nonlocal cur,ans
            if not node: return
            inorder(node.left)
            cur += 1
            if k == cur:
                ans = node.val
                return
            
            inorder(node.right)
        inorder(root)
        return ans