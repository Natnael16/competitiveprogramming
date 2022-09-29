class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
#         r = s[::-1]
        str_len = len(s)
#         top_down approach
#         @lru_cache(None)
#         def dp(p1, p2):
#             if p1 >= str_len or p2 >= str_len:
#                 return 0
#             if s[p1] == r[p2]:
#                 return 1 + dp(p1 + 1, p2 + 1)
#             else:
#                 return max(dp(p1 + 1, p2), dp(p1, p2 + 1))
#         return dp(0,0)
        
    
        #bottom up approach        
        dp = [[0] * (str_len + 1) for _ in range(str_len + 1)]
        for front in range(1, str_len + 1):
            for back in range(1 , str_len + 1):
                if s[front - 1] == s[str_len - (back)]:
                    dp[front][back] = dp[front- 1][back - 1] + 1
                else:
                    dp[front][back] = max(dp[front- 1][back], dp[front][back - 1])
 
        return dp[-1][-1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
               
    
    