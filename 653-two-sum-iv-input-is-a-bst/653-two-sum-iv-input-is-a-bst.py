# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], target: int) -> bool:
        seen = set()
        q = deque([root])
        while q:
            cur = q.pop()
            if not cur: continue
            if target - cur.val in seen: return True
            seen.add(cur.val)
            q.append(cur.left)
            q.append(cur.right)