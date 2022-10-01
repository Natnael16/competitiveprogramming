class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}
        
        def dp(i):
            if i == len(s): return 1
            if i in memo: return memo[i]
            
            if s[i] == '0': 
                memo[i] = 0
                return 0
            
            if i == len(s)-1:
                return 1
                    
            
            if int(s[i:i+2]) > 26:
                res = dp(i+1)
                
            else:
                res = dp(i+1) + dp(i+2)
                
            memo[i] = res
            
            return res
        
        return dp(0)