# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return 
        if key == root.val:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            
        node = root
        parent = None
        while node:
            if node.val == key:
                break
            elif key > node.val:
                parent = node
                node = node.right
            else:
                parent = node
                node = node.left
                
        if not node: return root
        
        if not node.right and not node.left:
            if parent.left and parent.left.val == key:
                parent.left = None
                return root
            else:
                parent.right = None
                return root
        if not node.right:
            if parent.left and parent.left.val == key:
                parent.left = node.left
                return root
            else:
                parent.right = node.left
                return root
        elif not node.left:
            if parent.left and parent.left.val == key:
                parent.left = node.right
                return root
            else:
                parent.right = node.right
                return root
    
        temp = node.right
        
        while temp.left:
            temp = temp.left
        node.val = temp.val
        
        p = node
        
        find = node.right
        
        while find:
            if find.val == temp.val:
                break
            elif temp.val > find.val:
                p = find
                find = find.right
            else:
                p = find
                find = find.left
                
        if not find.right and not find.left:
            
            if p.left and p.left.val == temp.val:
                p.left = None
                return root
            else:
                p.right = None
                return root
        if not find.right:
            if p.left and p.left.val == temp.val:
                p.left = find.left
                return root
            else:
                p.right = find.left
                return root
        elif not find.left:
            if p.left and p.left.val == temp.val:
                p.left = find.right
                return root
            else:
                p.right = find.right
                return root
        
        
        
 