class Solution:
    def getXor(self,nums):
        xor = 0
        for num in nums:
            xor ^= num
        return xor
    def getfirstOnPos(self,xor):
        get_bit = 1
        count = 0
        for _ in range(32):
            if get_bit & xor:
                break
            count += 1
            get_bit <<=1
        return 1 << count
        
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        xor = self.getXor(nums)
        check_bit = self.getfirstOnPos(xor)
        
        num1, num2 = 0, 0
        
        for num in nums:
            if check_bit & num:
                num1 ^= num
            else:
                num2 ^= num
                
        return [num1,num2]
            
        
        