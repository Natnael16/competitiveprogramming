class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n-2,-1,-1):
            maxi = -inf
            for j in range(i,n):
                if nums[i] < nums[j]:
                    maxi = max(maxi, dp[j])
            if maxi != -inf: dp[i] += maxi
        return max(dp)
                
        