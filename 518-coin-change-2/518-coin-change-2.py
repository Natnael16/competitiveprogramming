class Solution:
    
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(maxsize = None)
        def dp(target , ind):
            if target < 0: return 0
            if target == 0:
                return 1
            allsum = 0
            for i  in range(ind , len(coins)):
                if target - coins[i] >=0:
                    allsum += dp(target - coins[i] , i)
            return allsum
        return dp(amount ,0)