class Solution:
    def jump(self, nums: List[int]) -> int:
        # [2,2,1,1,4]
        # [0,1,2,1,0]    
        #         n = len(nums) TLE
        #         @lru_cache(None)
        #         def dp(ind):
        #             if ind == n -1: return 0
        #             mini = inf
        #             for num in range(1,nums[ind] + 1 ):
        #                 if num + ind < n:
        #                     mini = min(mini ,dp(num + ind) + 1)
        #             return mini
        #         return dp(0)
        n = len(nums)
        dp = [0] * n
        for i in range(n-2, -1,-1):
            if nums[i] + i >= n-1:
                dp[i] = 1
                continue
            mini = inf
            for j in range(1,nums[i] + 1 ):
                if j + i < n:
                    mini = min(mini,dp[j + i] + 1)
            dp[i] = mini
        # print(dp)
        return dp[0]
                
                
    
        
    
                
        