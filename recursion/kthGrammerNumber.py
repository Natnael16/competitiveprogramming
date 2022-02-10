from functools import lru_cache
@lru_cache(16)
class Solution(object):
    @lru_cache(maxsize = 16)
    def kthGrammar(self,n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0: return 0
        parent = self.kthGrammar(n-1, k//2 + k%2)
        if k % 2 == 1:
            parity = 'odd'
        else:
            parity = 'even'
        if parent == 0:
            if parity == 'odd':
                return 0
            else:
                return 1
        elif parent == 1:
            if parity == 'odd':
                return 1
            else:
                return 0