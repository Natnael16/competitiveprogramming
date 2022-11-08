class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number = 0
        shift = 1
        neg_count = 0
        for _ in range(32):
            one_count = 0
            for num in nums:
                if num < 0:
                    neg_count += 1
                if num & shift:
                    one_count += 1
            
            if one_count % 3:
                number |= shift
            shift <<= 1
            
        return number - 2**32 if neg_count % 3 else number
    
            
          
        