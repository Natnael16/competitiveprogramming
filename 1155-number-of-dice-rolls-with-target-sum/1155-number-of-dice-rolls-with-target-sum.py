class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        nums = [i for i in range(1,k+1)]
        @lru_cache(None)
        def dp(tar , freq):
            if tar <=0 or freq == 0:
                if tar == 0 and freq == 0:
                    return 1
                return 0
            tot = 0
            for num in nums:
                tot += dp(tar - num, freq -1)
            return tot
        return dp(target,n) % (10**9 + 7)