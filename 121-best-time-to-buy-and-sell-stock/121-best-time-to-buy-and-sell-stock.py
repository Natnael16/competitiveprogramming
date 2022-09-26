class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]    
        ans = 0
        for i in range(1,len(prices)):
            if prices[i] > mini:
                ans = max(ans, prices[i] - mini)
            else:
                mini = prices[i]
        return ans