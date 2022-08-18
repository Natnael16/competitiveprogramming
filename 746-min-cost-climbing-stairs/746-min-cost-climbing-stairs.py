class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #top down 
        if len(cost) == 1: return cost[0]
        cost.append(0)
        @lru_cache(None)
        def dp(take): 
            if take >= len(cost) - 1:
                return 0
            return cost[take] + min(dp(take + 1) , dp(take + 2))
        return dp(-1)
            
            