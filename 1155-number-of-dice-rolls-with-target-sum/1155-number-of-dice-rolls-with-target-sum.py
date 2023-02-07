class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        
        @lru_cache(None)
        def dp(cur_tar,tries):
            if cur_tar == 0 and tries == 0:
                return 1
            if cur_tar < 0 or tries == 0:
                return 0
            count = 0
            for page in range(1,k+1):
                count += dp(cur_tar - page,tries - 1)
            return count % mod
        return dp(target,n)
            
            
            
