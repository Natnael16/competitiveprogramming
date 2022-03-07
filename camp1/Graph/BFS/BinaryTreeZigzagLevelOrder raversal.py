# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        q = deque([root])
        level = []
        res = [[root.val]]
        countLevel = 1
        while q or level:
            if not q:
                if countLevel % 2 == 0:
                    res.append([i.val for i in level])
                else:
                    res.append([i.val for i in level[::-1]])

                countLevel += 1
                q.extend(level)
                level.clear()
            cur = q.popleft()
            if cur.left:
                level.append(cur.left)
            if cur.right:
                level.append(cur.right)
        return res