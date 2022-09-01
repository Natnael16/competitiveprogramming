# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # self.count = 0
        # def dfs(node, greatest):
        #     if not node: return 
        #     if node.val >= greatest: self.count += 1
        #     dfs(node.left , max(greatest, node.val))
        #     dfs(node.right , max(greatest, node.val))
        # dfs(root,-inf)
        # return self.count
        count = 0
        stack = [(root,-inf)]
        while stack:
            node , greatest = stack.pop()
            if node.val >= greatest: count += 1
            if node.left:
                stack.append((node.left, max(greatest,node.val)))
            if node.right:
                stack.append((node.right, max(greatest,node.val)))
        return count