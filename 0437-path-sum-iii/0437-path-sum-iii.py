# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        
        path_sum = 0
        def dfs(node, psum, prefix_dict):
            nonlocal path_sum
            if not node:
                return
            
            psum += node.val
            prefix_to_delete = psum - targetSum 
            if prefix_to_delete in prefix_dict:
                path_sum += prefix_dict[prefix_to_delete]
            prefix_dict[psum] += 1
            dfs(node.left ,psum , prefix_dict)
            dfs(node.right , psum , prefix_dict)
            
            prefix_dict[psum] -= 1
        dfs(root, 0 , prefix_sum)
        return path_sum
                
            
                
            
        