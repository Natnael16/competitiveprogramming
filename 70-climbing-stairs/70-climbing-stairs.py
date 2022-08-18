class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def climb(n):
            if n == 0 or n == 1: return n
            elif n == 2: return 2
            elif n > 2:
                return climb(n - 2) + climb(n - 1)

        return climb(n)







