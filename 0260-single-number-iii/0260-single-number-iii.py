class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        get_bit = 1
        count = 0
        for _ in range(32):
            if get_bit & xor:
                break
            count += 1
            get_bit <<=1
        
        num1, num2 = 0, 0
        check_bit = 1 << count
        for num in nums:
            if check_bit & num:
                num1 ^= num
            else:
                num2 ^= num
        return [num1,num2]
            
        
        