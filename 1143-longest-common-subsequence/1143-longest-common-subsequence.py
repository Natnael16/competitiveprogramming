class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ''' a b c d e
            a 1 1 1 1 1
            b 1 2 2 2 2
            c 1 2 3 3 3
            ''' 
        
        n,m = len(text1) , len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        
        for t1 in range(1,n + 1 ):
            for t2 in range(1, m + 1):
                if text1[t1 - 1] == text2[t2 - 1]:
                    dp[t1][t2] = dp[t1-1][t2- 1] + 1
                else:
                    dp[t1][t2] = max(dp[t1-1][t2], dp[t1][t2 - 1])
        return dp[-1][-1]