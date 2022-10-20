class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nums_len = len(nums)
        dp = [0] * (nums_len + 1)
        max_sum = -inf
        
        for back in range(nums_len - 1, -1 , -1):
            dp[back] = max((nums[back] + dp[back + 1] ,nums[back]))
            max_sum = max(max_sum,dp[back])
        return max_sum