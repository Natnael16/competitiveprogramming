class Solution:
    def isPowerOfFour(self, n: int) -> bool:
#         16 // 4  - 4/4 - 1 
#         # base case
#         n == 1 -> True
#         #base case
#         n % 4 != 0 -> False
        
    
#         # return number / 4
        if n == 0:
            return False
        if n == 1:
            return True
        elif n % 4 != 0:
            return False
        else:
            return self.isPowerOfFour(n//4)
        