class Solution:

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        
        """
        inorder = []
        inorder_val = []

        def dfs(root):
            if not root: return

            dfs(root.left)
            inorder.append(root)
            inorder_val.append(root.val)
            dfs(root.right)

        dfs(root)
        inorder_val.sort()
        i = 0
        while i < len(inorder_val):
            inorder[i].val = inorder_val[i]
            i += 1
