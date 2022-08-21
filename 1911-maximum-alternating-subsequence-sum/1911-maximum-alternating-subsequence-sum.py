class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        '''[4 , 2 ,5, 3]
        
        4 , odd , sums even and odd
            2 , 5 , 3
            
            
        base case if len == 1 return even - odd
                    out of bound return 0
        '''

#         @lru_cache(None)
#         def dp(ptr, isEven):
#             if ptr == len(nums): return 0
#             num = nums[ptr] if isEven else -nums[ptr]
            
#             return max(num + dp(ptr + 1 , not isEven) , dp(ptr + 1 , isEven))
#         return dp(0 ,True)
        
        #bottom up
        sumOdd , sumEven = 0 , 0
        
        for i in range(len(nums) - 1 ,-1, -1):
            sumOdd = max(sumEven-nums[i] , sumOdd)
            sumEven = max(sumOdd + nums[i] , sumEven)
        return max(sumOdd , sumEven)