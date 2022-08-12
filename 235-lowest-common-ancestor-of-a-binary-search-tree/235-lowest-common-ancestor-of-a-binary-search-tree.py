# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    
        def helper(node , p , q):
            if p.val <= node.val and q.val >= node.val or p.val >= node.val and q.val <= node.val:
                return node.val
            
            if p.val < node.val and q.val < node.val: return helper(node.left , p , q)
            elif p.val > node.val and q.val > node.val: return helper(node.right , p , q)
            
        return TreeNode(val = helper(root , p ,q ))
            
            #i will check if p <= node.val and q>= node.val or p >= node.val and q <= node.val
                # if true return node.val
                
            # if both > node.val: return  go right
            #if both < node.val: return go left
            
            
            
          
            
            