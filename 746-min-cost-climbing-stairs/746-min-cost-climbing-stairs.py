class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #top down 
        # if len(cost) == 1: return cost[0]
        # cost.append(0)
        # @lru_cache(None)
        # def dp(take): 
        #     if take >= len(cost) - 1:
        #         return 0
        #     return cost[take] + min(dp(take + 1) , dp(take + 2))
        # return dp(-1)
        #bottom up
        
        top = 0
        last = cost[-1]
        for i in range(len(cost) - 2 , -1 , -1):
            new = cost[i] + min(last , top)
            top = last
            last = new
        return min(last , top)
            
            