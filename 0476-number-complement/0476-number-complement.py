class Solution:
    def findComplement(self, num: int) -> int:
        
        ans = 0
        shift = 1
        while shift < num:
            if not (shift & num):
                ans = ans | shift
            shift = shift << 1
        return ans
    
                