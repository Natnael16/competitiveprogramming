class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dp(tar):
            if tar == 0 : return 1
            if tar < 0 : return 0
            tot = 0
            for num in nums:
                tot += dp(tar - num)
            return tot
        return dp(target)