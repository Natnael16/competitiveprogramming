# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], target: int) -> bool:
        nums = []
        def preorder(node):
            if not node: return 
            
            preorder(node.left)
            nums.append(node.val)
            preorder(node.right)
        preorder(root)
        
        front , back = 0, len(nums) - 1
        while front < back:
            if nums[front ] + nums[back] > target:
                back -= 1
            elif nums[front] + nums[back] < target:
                front += 1
            else: return True
        return False
            