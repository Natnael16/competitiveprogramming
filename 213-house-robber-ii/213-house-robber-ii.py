class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(ind, dontUse):
            
            if ind >= len(nums): return 0
            
            if ind == len(nums) - 1 and dontUse:
                return 0
            
            if ind == 0:
                use = nums[ind] + dp(ind + 2 , True)
            else:
                use = nums[ind] + dp(ind + 2 , dontUse)
            return max(use , dp(ind + 1 , dontUse))
        
        return dp(0 , False)
            