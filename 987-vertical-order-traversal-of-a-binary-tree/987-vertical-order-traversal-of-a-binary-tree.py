# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class ThreeNum:
    def __init__(self,one, two, three):
        self.one = one
        self.two = two
        self.three = three
    def __str__(self):
        return str(self.three)
    def __lt__(self,other):
    
        if self.one < other.one:
            return True
        elif self.one == other.one:
            if self.two < other.two:
                return True
            elif self.two == other.two:
                if self.three < other.three:
                    return True
            

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.column_dict = defaultdict(list)
        
        def dfs(node, coord):
            if not node: return
            self.column_dict[coord[1]].append(ThreeNum(coord[1], coord[0] , node.val))
            dfs(node.left, (coord[0] + 1 , coord[1] - 1))
            dfs(node.right, (coord[0] + 1, coord[1] + 1))
        dfs(root , (0,0))
        ans = []
        for d in self.column_dict:
            ans.append(self.column_dict[d])
        ans.sort()
        res = []
        for a in ans:
            nested = []
            for j in a:
                nested.append(j)
            res.append(sorted(nested))
        return res
                