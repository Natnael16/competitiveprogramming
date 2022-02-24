class Solution:

    def rob(self, nums: List[int]) -> int:
        dp = []
        dp.append(0)
        dp.append(nums[0])
        for i in range(1, len(nums)):
            dp.append(max(dp[i], dp[i - 1] + nums[i]))
        return dp[-1]