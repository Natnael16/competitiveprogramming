# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        ans = []
        while q:
            tot = 0
            count = len(q)
            for i in range(count):
                cur = q.popleft()
                tot += cur.val
                if cur.right: q.append(cur.right)
                if cur.left: q.append(cur.left)
            ans.append(tot/count)
        return ans
    