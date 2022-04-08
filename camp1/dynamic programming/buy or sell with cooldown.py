# from functools import lru_cache
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        # @lru_cache
        cache = {}

        def dfs(ind, isBuying):
            if ind > len(prices) - 1: return 0
            if (ind, isBuying) in cache:
                return cache[(ind, isBuying)]

            if isBuying:
                buy = dfs(ind + 1, not isBuying) - prices[ind]
                cool = dfs(ind + 1, isBuying)
                cache[(ind, isBuying)] = max(buy, cool)
            else:
                sell = dfs(ind + 2, not isBuying) + prices[ind]
                cool = dfs(ind + 1, isBuying)

                # print(dfs.cache_info())
                cache[(ind, isBuying)] = max(sell, cool)
            return cache[(ind, isBuying)]

        return dfs(0, True)
