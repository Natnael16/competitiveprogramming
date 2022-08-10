# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # make the middle element the root 
        # starting from index 0 add every thing to left 
        # starting from index -1 add every thing to right of the tree
        
        def buildBST(left , right):
            
            if left > right: return
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = buildBST(left , mid - 1)
            root.right = buildBST(mid + 1 , right)
            return root
                                  
        return buildBST(0 , len(nums)-1)
    