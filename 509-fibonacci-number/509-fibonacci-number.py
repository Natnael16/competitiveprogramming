from functools import lru_cache
class Solution:
    @lru_cache
    def fib(self, n: int) -> int:
        if n == 0 or n == 1: return n
        zero = 0
        one = 1
        for i in range(n - 1):
            three = zero + one
            zero , one = one , zero
            one = three
        return one
            
            
   