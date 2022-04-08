class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        t = []

        while q or t:
            if not q:
                # checking
                i = 0
                j = len(t) - 1
                while i < j:
                    if (not t[i] and not t[j]) or ((t[i] and t[j])
                                                   and t[i].val == t[j].val):
                        i += 1
                        j -= 1
                    else:
                        return False
                q.extend(t)
                t = []

            curr = q.popleft()
            if curr:
                t.append(curr.left)
                t.append(curr.right)

        return True