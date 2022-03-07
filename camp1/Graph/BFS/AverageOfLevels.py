class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        level = []
        average = [root.val]
        while q or level:
            if not q:
                tot = 0
                count = 0
                for i in level:
                    if i:
                        count += 1
                        tot += i.val

                average.append(tot / count)
                q.extend(level)
                level = []
            cur = q.popleft()
            if cur.left:
                level.append(cur.left)
            if cur.right:
                level.append(cur.right)
        return average