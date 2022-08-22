class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
#         tar 11
#         for all of them
#             amount - num[cur]
#             10 
#             in base if amount == 0: retrun 1 else inf
                
    
#             return min of all possible
        @lru_cache(None)
        def dp(amount):
            if amount < 0: return float("inf")
            if amount == 0: return 1
            
            mini = float('inf')
            for coin in coins:
                mini = min(mini , dp(amount - coin))
            return mini + 1
        ans = dp(amount)
        if ans  != float("inf"):
            return ans -1
        return -1
    