class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @lru_cache(1000)
        def hel(n, target):
            if target < n or target > n*k:
                return 0 
            if n == 1:
                return 1
            
            s = 0 
            for i in range(1, k+1): 
                s += hel(n-1, target-i) 
            return s
            
        return int(hel(n, target)) % (10**9 + 7)