class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        '''
        
        [[0 , 0 , 0 ],
         [0 , 0 , 0]
         [0 , 0 , 0]]
        '''
        m, n = len(multipliers), len(nums)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
 
        
        for mul in range(m - 1 , -1 , -1):
            for left in range(mul , -1 , -1 ):
                
                dp[mul][left] = max(nums[n-1 - (mul - left)] * multipliers[mul] + dp[mul + 1][left],
                                   nums[left] * multipliers[mul] + dp[mul + 1][left + 1])
        
        return dp[0][0]
#         memo = {}

#         def dfs(l,m): 
            
#             if (l, m ) in memo: return memo[(l,m)]
#             if m == len(multipliers): return 0
#             memo[(l,m)] = max(nums[l] * multipliers[m] + dfs(l + 1, m + 1),
#                       nums[len(nums) - 1 - (m - l)] * multipliers[m] + dfs(l , m + 1))
#             return memo[(l,m)]
#         return dfs(0, 0)


            