"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q = deque([root])
        ans = []
        while q:
            inside = []
            for i in range(len(q)):
                cur = q.popleft()
                if cur:
                    inside.append(cur.val)
                    for child in cur.children:
                        if child:
                            q.append(child)
            if inside:
                ans.append(inside)

        return ans
    
                
                                
        
        
        