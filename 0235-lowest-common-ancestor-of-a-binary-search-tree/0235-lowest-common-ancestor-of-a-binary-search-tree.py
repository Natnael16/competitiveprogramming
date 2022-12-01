# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @lru_cache(None)
    def find(self,node,target):
            if not node:
                return False
            if node.val == target:
                return True
            return self.find(node.left, target) or self.find(node.right,target)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return 

        if root.val == p.val or root.val == q.val:
            return root
        lp, rq, lq,rp = self.find(root.left, p.val),self.find(root.right, q.val),self.find(root.left, q.val),self.find(root.right, p.val)
      
        if (lp and rq) or (lq and rp):
            return root
        if self.find(root.left,p.val):
            return self.lowestCommonAncestor(root.left, p , q)
        else:
            return self.lowestCommonAncestor(root.right, p , q)
    
        
        
        
            
          
            
            
          
            
            