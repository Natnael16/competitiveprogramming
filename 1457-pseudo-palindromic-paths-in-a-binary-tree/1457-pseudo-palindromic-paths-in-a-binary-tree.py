# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        '''
        palindromic 
        123322
        if lenght even
            all of the numbers have even count
        if length odd
            only one number have odd count
        
        iterate untill you reach leaf node then calculate whether it is or it is not
        on my way I can keep track dictionary with count of those numbers 
        
        add self
        {2: 1}
        then check
        1121111
        '''
        self.count = 0
        def isPal(node, counter):
            if not node: return 
            
            counter[node.val] += 1
            
            
            if not node.left and not node.right:           
                oddCount = 0
                total = 0
                for num in counter:
                    if counter[num] % 2 != 0: oddCount += 1
                    total += counter[num]
                if total % 2 == 0 and oddCount == 0: self.count += 1
                elif oddCount == 1: self.count += 1                    
                    
            leftCounter = copy.deepcopy(counter)
            rightCounter = copy.deepcopy(counter)
            counter.clear()
            isPal(node.left,leftCounter)
            isPal(node.right,rightCounter)
        isPal(root , defaultdict(int))
        return self.count
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        