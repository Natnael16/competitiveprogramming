class Solution:
    def countOrders(self, n: int) -> int:
        @lru_cache(None)
        def counter(pick , deliver):
            if not pick and not deliver: return 1
            
            elif not pick and deliver:
                return deliver * counter(pick , deliver - 1)
            elif not deliver and pick:
                return pick * counter(pick - 1 , deliver + 1)
            else:
                return pick * counter(pick - 1 , deliver + 1)  + deliver * counter(pick , deliver - 1)
        return counter(n , 0) % (10**9 + 7)