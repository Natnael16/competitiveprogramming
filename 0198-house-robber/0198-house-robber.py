class Solution:
    def rob(self, nums: List[int]) -> int:
    # skip and move to right 
    # or move right + 1
        memo = {}
        def dp(take):
            if take in memo: return memo[take]
            if take >= len(nums):
                memo[take] = 0
                return 0
            res =  max(dp(take + 1) , nums[take] + dp(take + 2))
            memo[take] = res
            return res
        return dp(0)