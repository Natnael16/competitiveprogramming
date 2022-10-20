class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        nums_len = len(nums)
        dp = [[0,0] for _ in range(nums_len + 1)] #max and min so far
        
        max_sum = -inf
        for back in range(nums_len - 1,-1,-1):
            min_so_far , max_so_far = dp[back + 1]
            dp[back][0] = min(nums[back],nums[back] + min_so_far)
            dp[back][1] = max(nums[back],nums[back] + max_so_far)
            max_sum = max(abs(dp[back][0]), abs(dp[back][1]),max_sum)
        return max_sum
            
            
            