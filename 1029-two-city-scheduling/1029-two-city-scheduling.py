class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        @lru_cache(None)
        def getMinCost(aCount , bCount):
            total_count = aCount + bCount
            if total_count == len(costs):
                return 0 if aCount == bCount else inf
            return min(getMinCost(aCount + 1, bCount) + costs[total_count][0],getMinCost(aCount, bCount + 1) + costs[total_count][1] )
        return getMinCost(0,0)