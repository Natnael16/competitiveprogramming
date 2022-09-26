class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]    
        self.ans = 0
        for i in range(1,len(prices)):
            if prices[i] > mini:
                if prices[i] - mini > self.ans:
                    self.ans = prices[i] - mini
            else:
                mini = prices[i]
        return self.ans