class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step1 = 0
        step2 = 0
        for i in range(len(cost) - 1, -1, -1):
            cur_step = cost[i] + min(step1, step2)
            step2 = step1
            step1 = cur_step
        return min(step1, step2)
