class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val == val:
                break
            elif root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
        return root
