class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        '''
        if buy false 
                buy or skip 
            if buy true
                sell or skip
            if k reach max or 
            return max profit
        '''
        memo = {}
        def maxP(ind , bought , transaction):
            if (ind, bought , transaction) in memo: return memo[(ind, bought, transaction)]
            if transaction > k or  ind > len(prices) - 1: return 0

            if not bought:
                memo[(ind,bought,transaction)] =   max(-prices[ind] + maxP(ind + 1, not bought, transaction + 1) ,maxP(ind + 1 , bought , transaction))
            else:
                 memo[(ind,bought,transaction)] = max(prices[ind] + maxP(ind + 1, not bought, transaction ), maxP(ind + 1 , bought , transaction))
            return memo[(ind,bought,transaction)]
        return maxP(0,False , 0)