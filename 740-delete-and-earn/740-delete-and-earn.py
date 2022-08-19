class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = dict(Counter(nums))
        count_feq = sorted(list(counter.items()))
        memo = {}
        def dp(take):
            if take >= len(count_feq):
                return 0
            if take not in memo:
                if take == len(count_feq) - 1:
                    memo[take] =  count_feq[-1][0] * count_feq[-1][1]
                    return memo[take]
                elif -count_feq[take][0] + count_feq[take + 1][0] > 1:

                    memo[take] =  (count_feq[take][0] * count_feq[take][1]) + dp(take + 1)

                else:
                    memo[take] = max((count_feq[take][0] * count_feq[take][1]) + dp(take + 2) , dp(take + 1))
            return memo[take]
        return dp(0)
            

        