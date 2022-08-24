class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache(None)
        def dp(ind ):
            if ind == len(days): return 0
            
            ans = inf
            
            for i , day in enumerate([1,7,30]):
                j = ind
                while j < len(days) and day + days[ind] > days[j]:
                    j+=1
                ans = min(ans , costs[i] + dp(j))
            return ans
        return dp(0)
            