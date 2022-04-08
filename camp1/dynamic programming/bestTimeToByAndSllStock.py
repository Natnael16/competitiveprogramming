class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        sell = sys.maxsize
        max_p = 0
        for i in prices:
            if i < sell:
                sell = i
            else:
                max_p = max(max_p, i - sell)
        return max_p
