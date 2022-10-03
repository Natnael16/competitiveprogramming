class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # top_down
        # @lru_cache(None)
        # def dp(ind):
        #     if ind == len(nums) - 1:return True
        #     elif ind >= len(nums): return False
        #     flag = False
        #     for i in range(ind + 1,nums[ind] + ind + 1):
        #         flag = flag or dp(i)
        #     return flag
        # return dp(0)
        
        #bottomup
        # [0,0,0,0,1]
        # cur + num[cur] >= true_ind make me  true
        n = len(nums)
        
        dp = [False] * n
        dp[-1] = True
        true_ind = n -1
        for back_idx in range(n-2,-1,-1):
            if nums[back_idx] + back_idx >= true_ind:
                dp[back_idx] = True
                true_ind = back_idx
        return dp[0]